# EDSProvider.GetSignedDocumentAsync - метод
Возвращает объект в base64, содержащий ЭП подписанного файла.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual ValueTask<string> GetSignedDocumentAsync(
    	string signatureBase64,
    	string fileBase64,
    	string certificateBase64,
    	DateTime signingTime,
    	string digestAlgorithm = null,
    	string encryptionAlgorithm = null,
    	Dictionary<string, Object> info = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function GetSignedDocumentAsync ( 
    	signatureBase64 As String,
    	fileBase64 As String,
    	certificateBase64 As String,
    	signingTime As DateTime,
    	Optional digestAlgorithm As String = Nothing,
    	Optional encryptionAlgorithm As String = Nothing,
    	Optional info As Dictionary(Of String, Object) = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As ValueTask(Of String)
C++ __Копировать
     public:
    virtual ValueTask<String^> GetSignedDocumentAsync(
    	String^ signatureBase64, 
    	String^ fileBase64, 
    	String^ certificateBase64, 
    	DateTime signingTime, 
    	String^ digestAlgorithm = nullptr, 
    	String^ encryptionAlgorithm = nullptr, 
    	Dictionary<String^, Object^>^ info = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract GetSignedDocumentAsync : 
            signatureBase64 : string * 
            fileBase64 : string * 
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
    override GetSignedDocumentAsync : 
            signatureBase64 : string * 
            fileBase64 : string * 
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
fileBase64 [String](https://learn.microsoft.com/dotnet/api/system.string)
    Подписываемый файл в base64.
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
Объект в base64, содержащий ЭП подписанного файла.
#### Реализации
[IEDSProvider.GetSignedDocumentAsync(String, String, String, DateTime, String,
String, Dictionary<String, Object>,
CancellationToken)](M_Tessa_Platform_EDS_IEDSProvider_GetSignedDocumentAsync.htm)  
##  __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
