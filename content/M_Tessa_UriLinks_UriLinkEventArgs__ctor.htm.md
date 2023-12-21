# UriLinkEventArgs - конструктор
Создаёт экземпляр объекта
[UriLinkEventArgs](T_Tessa_UriLinks_UriLinkEventArgs.htm).
## __Definition
 **Пространство имён:** [Tessa.UriLinks](N_Tessa_UriLinks.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public UriLinkEventArgs(
    	Uri uri,
    	bool cancel = false
    )
VB __Копировать
     Public Sub New ( 
    	uri As Uri,
    	Optional cancel As Boolean = false
    )
C++ __Копировать
     public:
    UriLinkEventArgs(
    	Uri^ uri, 
    	bool cancel = false
    )
F# __Копировать
     new : 
            uri : Uri * 
            ?cancel : bool 
    (* Defaults:
            let _cancel = defaultArg cancel false
    *)
    -> UriLinkEventArgs
#### Параметры
uri [Uri](https://learn.microsoft.com/dotnet/api/system.uri)
    Объект [Uri](P_Tessa_UriLinks_UriLinkEventArgs_Uri.htm), описывающий обрабатываемую ссылку.
cancel [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
(Optional)
    Признак того, что действие отменяется.
##  __См. также
#### Ссылки
[UriLinkEventArgs - ](T_Tessa_UriLinks_UriLinkEventArgs.htm)
[Tessa.UriLinks - пространство имён](N_Tessa_UriLinks.htm)
