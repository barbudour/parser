# ScanDocumentHelper.GetPageName - метод
Возвращает имя страницы по умолчанию, доступной по индексу, отсчитываемому от
нуля. Для того, чтобы получить имя файла со страницей, добавьте расширение с
ведущей точкой (обычно используется метод
[GetPageFileName(Int32)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_GetPageFileName.htm)).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static string GetPageName(
    	int index
    )
VB __Копировать
     Public Shared Function GetPageName ( 
    	index As Integer
    ) As String
C++ __Копировать
     public:
    static String^ GetPageName(
    	int index
    )
F# __Копировать
     static member GetPageName : 
            index : int -> string 
#### Параметры
index [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
    Индекс страницы, отсчитываемый от нуля.
#### Возвращаемое значение
[String](https://learn.microsoft.com/dotnet/api/system.string)  
Имя страницы по умолчанию.
##  __См. также
#### Ссылки
[ScanDocumentHelper -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
