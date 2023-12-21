# CardTaskDialogHelper.GetFileContentFromInfo - метод
Возвращает контент файла диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)) представленный в виде
строки в Base64.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static string? GetFileContentFromInfo(
    	CardInfoStorageObject infoStorageObject
    )
VB __Копировать
     Public Shared Function GetFileContentFromInfo ( 
    	infoStorageObject As CardInfoStorageObject
    ) As String
C++ __Копировать
     public:
    static String^ GetFileContentFromInfo(
    	CardInfoStorageObject^ infoStorageObject
    )
F# __Копировать
     static member GetFileContentFromInfo : 
            infoStorageObject : CardInfoStorageObject -> string 
#### Параметры
infoStorageObject
[CardInfoStorageObject](T_Tessa_Cards_CardInfoStorageObject.htm)
    Объект, содержащий получаемую информацию.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Контент файла диалога с временем жизни "Запрос"
([Info](T_Tessa_Cards_CardTaskDialogStoreMode.htm)) представленный в виде
строки в Base64 или значение по умолчанию для типа, если его не удалось
получить.
##  __См. также
#### Ссылки
[CardTaskDialogHelper - ](T_Tessa_Cards_CardTaskDialogHelper.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
