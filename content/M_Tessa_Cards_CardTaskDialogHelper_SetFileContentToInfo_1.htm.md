# CardTaskDialogHelper.SetFileContentToInfo(CardInfoStorageObject, String,
CardFileVersion) - метод
Задаёт информацию о файле диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFileContentToInfo(
    	CardInfoStorageObject infoStorageObject,
    	string base64FileContent,
    	CardFileVersion fileVersion
    )
VB __Копировать
     Public Shared Sub SetFileContentToInfo ( 
    	infoStorageObject As CardInfoStorageObject,
    	base64FileContent As String,
    	fileVersion As CardFileVersion
    )
C++ __Копировать
     public:
    static void SetFileContentToInfo(
    	CardInfoStorageObject^ infoStorageObject, 
    	String^ base64FileContent, 
    	CardFileVersion^ fileVersion
    )
F# __Копировать
     static member SetFileContentToInfo : 
            infoStorageObject : CardInfoStorageObject * 
            base64FileContent : string * 
            fileVersion : CardFileVersion -> unit 
#### Параметры
infoStorageObject
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект, в котором должна быть сохранена информация о файле.
base64FileContent
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Контент файла в Base64.
fileVersion [CardFileVersion](T_Tessa_Cards_CardFileVersion.htm)
    Информация о версии файла.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[SetFileContentToInfo -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_SetFileContentToInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
