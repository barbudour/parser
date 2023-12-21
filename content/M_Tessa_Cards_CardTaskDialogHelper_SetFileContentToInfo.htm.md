# CardTaskDialogHelper.SetFileContentToInfo(CardFile, Byte[], IUser) - метод
Задаёт контент файла карточки диалога с временем жизни
[Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetFileContentToInfo(
    	CardFile cardFile,
    	byte[] content,
    	IUser user
    )
VB __Копировать
     Public Shared Sub SetFileContentToInfo ( 
    	cardFile As CardFile,
    	content As Byte(),
    	user As IUser
    )
C++ __Копировать
     public:
    static void SetFileContentToInfo(
    	CardFile^ cardFile, 
    	array<unsigned char>^ content, 
    	IUser^ user
    )
F# __Копировать
     static member SetFileContentToInfo : 
            cardFile : CardFile * 
            content : byte[] * 
            user : IUser -> unit 
#### Параметры
cardFile [CardFile](T_Tessa_Cards_CardFile.htm)
    Информация о файле, контент которого требуется задать.
content [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
    Задаваемый контент файла.
user [IUser](T_Tessa_Platform_Runtime_IUser.htm)
Сессия пользователя.
## __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[SetFileContentToInfo -
перегрузка](Overload_Tessa_Cards_CardTaskDialogHelper_SetFileContentToInfo.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
