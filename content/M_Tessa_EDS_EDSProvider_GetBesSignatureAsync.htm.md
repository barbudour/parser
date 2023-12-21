# EDSProvider.GetBesSignatureAsync - метод
Возвращает подпись в формате BES в base64.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<string> GetBesSignatureAsync(
    	string signatureBase64,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetBesSignatureAsync ( 
    	signatureBase64 As String,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    virtual ValueTask<String^> GetBesSignatureAsync(
    	String^ signatureBase64, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetBesSignatureAsync : 
            signatureBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
    override GetBesSignatureAsync : 
            signatureBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
signatureBase64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Электронная подпись в base64.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры запроса к сервису или null, если параметры не указаны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[String](https://learn.microsoft.com/dotnet/api/system.string)>  
Подпись BES в формате base64.
#### Реализации
[IEDSProvider.GetBesSignatureAsync(String, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_GetBesSignatureAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
