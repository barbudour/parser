# EDSProvider.ExtendDocumentAsync - метод
Расширяет объект подписи информацией по меткам времени и другой информацией, в
соответствии с настройками. Возвращает расширенную подпись в base64,
информация о проверке подписи. Для подписи в формате BES возвращает исходную
подпись.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<(string ExtendedSignatureBase64, List<Dictionary<string, Object>> )> ExtendDocumentAsync(
    	string signatureBase64,
    	string certificateBase64,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function ExtendDocumentAsync ( 
    	signatureBase64 As String,
    	certificateBase64 As String,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of (ExtendedSignatureBase64 As String,  As List(Of Dictionary(Of String, Object))))
C++ __Копировать
     public:
    virtual ValueTask<ValueTuple<String^, List<Dictionary<String^, Object^>^>^>> ExtendDocumentAsync(
    	String^ signatureBase64, 
    	String^ certificateBase64, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ExtendDocumentAsync : 
            signatureBase64 : string * 
            certificateBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<string, List<Dictionary<string, Object>>>> 
    override ExtendDocumentAsync : 
            signatureBase64 : string * 
            certificateBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<ValueTuple<string, List<Dictionary<string, Object>>>> 
#### Параметры
signatureBase64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Электронная подпись в base64.
certificateBase64
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Сертификат в виде строки base64.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры запроса к сервису или null, если параметры не указаны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>>>  
Расширенная подпись в base64, информация о проверке подписи.
#### Реализации
[IEDSProvider.ExtendDocumentAsync(String, String, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_ExtendDocumentAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
