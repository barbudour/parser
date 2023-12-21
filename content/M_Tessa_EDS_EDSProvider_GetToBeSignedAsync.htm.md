# EDSProvider.GetToBeSignedAsync - метод
Возвращает объект подписи в base64, подготовленный для подписания на клиенте.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<string> GetToBeSignedAsync(
    	string signatureBase64,
    	string certificateBase64,
    	DateTime signingTime,
    	string digestAlgorithm = null,
    	string encryptionAlgorithm = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetToBeSignedAsync ( 
    	signatureBase64 As String,
    	certificateBase64 As String,
    	signingTime As DateTime,
    	Optional digestAlgorithm As String = Nothing,
    	Optional encryptionAlgorithm As String = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    virtual ValueTask<String^> GetToBeSignedAsync(
    	String^ signatureBase64, 
    	String^ certificateBase64, 
    	DateTime signingTime, 
    	String^ digestAlgorithm = nullptr, 
    	String^ encryptionAlgorithm = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetToBeSignedAsync : 
            signatureBase64 : string * 
            certificateBase64 : string * 
            signingTime : DateTime * 
            ?digestAlgorithm : string * 
            ?encryptionAlgorithm : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithm = defaultArg digestAlgorithm null
            let _encryptionAlgorithm = defaultArg encryptionAlgorithm null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
    override GetToBeSignedAsync : 
            signatureBase64 : string * 
            certificateBase64 : string * 
            signingTime : DateTime * 
            ?digestAlgorithm : string * 
            ?encryptionAlgorithm : string * 
            ?info : Dictionary<string, Object> * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithm = defaultArg digestAlgorithm null
            let _encryptionAlgorithm = defaultArg encryptionAlgorithm null
            let _info = defaultArg info null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTask<string> 
#### Параметры
signatureBase64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Электронная подпись в base64.
certificateBase64
[String](https://learn.microsoft.com/dotnet/api/system.string)
    Сертификат в виде строки base64.
signingTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
    Время подписания.
digestAlgorithm [String](https://learn.microsoft.com/dotnet/api/system.string)
(Optional)
    Алгоритм дайджеста.
encryptionAlgorithm
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
    Алгоритм шифрования.
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
Объект подписи в base64, подготовленный для подписания на клиенте.
#### Реализации
[IEDSProvider.GetToBeSignedAsync(String, String, DateTime, String, String,
Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_GetToBeSignedAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
