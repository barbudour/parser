# EDSProvider.ValidateDocumentAsync - метод
Выполняет валидацию электронной подписи. Возвращает сериализованную структуру,
которая содержит информацию по проверке различных параметров подписи.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<List<Dictionary<string, Object>>> ValidateDocumentAsync(
    	string signatureBase64,
    	SignatureType targetSignatureType,
    	SignatureProfile targetSignatureProfile,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function ValidateDocumentAsync ( 
    	signatureBase64 As String,
    	targetSignatureType As SignatureType,
    	targetSignatureProfile As SignatureProfile,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of List(Of Dictionary(Of String, Object)))
C++ __Копировать
     public:
    virtual ValueTask<List<Dictionary<String^, Object^>^>^> ValidateDocumentAsync(
    	String^ signatureBase64, 
    	SignatureType targetSignatureType, 
    	SignatureProfile targetSignatureProfile, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract ValidateDocumentAsync : 
            signatureBase64 : string * 
            targetSignatureType : SignatureType * 
            targetSignatureProfile : SignatureProfile * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<Dictionary<string, Object>>> 
    override ValidateDocumentAsync : 
            signatureBase64 : string * 
            targetSignatureType : SignatureType * 
            targetSignatureProfile : SignatureProfile * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<List<Dictionary<string, Object>>> 
#### Параметры
signatureBase64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Электронная подпись в base64.
targetSignatureType [SignatureType](T_Tessa_Platform_EDS_SignatureType.htm)
    Проверяемый тип подписи.
targetSignatureProfile
[SignatureProfile](T_Tessa_Platform_EDS_SignatureProfile.htm)
    Проверяемый профиль подписи.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
    Параметры запроса к сервису или null, если параметры не указаны.
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
    Объект, посредством которого можно отменить асинхронную задачу.
#### Возвращаемое значение
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)>>>  
Сериализованная структура, содержащая информацию по проверке параметров
подписи.
#### Реализации
[IEDSProvider.ValidateDocumentAsync(String, SignatureType, SignatureProfile,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_ValidateDocumentAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
