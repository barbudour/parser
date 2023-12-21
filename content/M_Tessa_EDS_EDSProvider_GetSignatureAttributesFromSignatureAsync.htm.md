# EDSProvider.GetSignatureAttributesFromSignatureAsync - метод
Возвращает параметры подписи для указанного объекта подписи.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<SignatureAttributes> GetSignatureAttributesFromSignatureAsync(
    	string signatureBase64,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetSignatureAttributesFromSignatureAsync ( 
    	signatureBase64 As String,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of SignatureAttributes)
C++ __Копировать
     public:
    virtual ValueTask<SignatureAttributes^> GetSignatureAttributesFromSignatureAsync(
    	String^ signatureBase64, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSignatureAttributesFromSignatureAsync : 
            signatureBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SignatureAttributes> 
    override GetSignatureAttributesFromSignatureAsync : 
            signatureBase64 : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<SignatureAttributes> 
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
[ValueTask](https://learn.microsoft.com/dotnet/api/system.threading.tasks.valuetask-1)<[SignatureAttributes](T_Tessa_Platform_EDS_SignatureAttributes.htm)>  
Параметры подписи.
#### Реализации
[IEDSProvider.GetSignatureAttributesFromSignatureAsync(String,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_GetSignatureAttributesFromSignatureAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
