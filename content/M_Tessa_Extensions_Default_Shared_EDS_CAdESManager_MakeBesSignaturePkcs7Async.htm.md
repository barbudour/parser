# CAdESManager.MakeBesSignaturePkcs7Async - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public Task<byte[]> MakeBesSignaturePkcs7Async(
    	byte[] certificate,
    	ISignatureFile file,
    	DateTime signingTime,
    	byte[] signature,
    	string digestAlgorithmOid = null,
    	string encryptionAlgorithmOid = null,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Function MakeBesSignaturePkcs7Async ( 
    	certificate As Byte(),
    	file As ISignatureFile,
    	signingTime As DateTime,
    	signature As Byte(),
    	Optional digestAlgorithmOid As String = Nothing,
    	Optional encryptionAlgorithmOid As String = Nothing,
    	Optional cancellationToken As CancellationToken = Nothing
    ) As Task(Of Byte())
C++ __Копировать
     public:
    virtual Task<array<unsigned char>^>^ MakeBesSignaturePkcs7Async(
    	array<unsigned char>^ certificate, 
    	ISignatureFile^ file, 
    	DateTime signingTime, 
    	array<unsigned char>^ signature, 
    	String^ digestAlgorithmOid = nullptr, 
    	String^ encryptionAlgorithmOid = nullptr, 
    	CancellationToken cancellationToken = CancellationToken()
    ) sealed
F# __Копировать
     abstract MakeBesSignaturePkcs7Async : 
            certificate : byte[] * 
            file : ISignatureFile * 
            signingTime : DateTime * 
            signature : byte[] * 
            ?digestAlgorithmOid : string * 
            ?encryptionAlgorithmOid : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithmOid = defaultArg digestAlgorithmOid null
            let _encryptionAlgorithmOid = defaultArg encryptionAlgorithmOid null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
    override MakeBesSignaturePkcs7Async : 
            certificate : byte[] * 
            file : ISignatureFile * 
            signingTime : DateTime * 
            signature : byte[] * 
            ?digestAlgorithmOid : string * 
            ?encryptionAlgorithmOid : string * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _digestAlgorithmOid = defaultArg digestAlgorithmOid null
            let _encryptionAlgorithmOid = defaultArg encryptionAlgorithmOid null
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> Task<byte[]> 
#### Параметры
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [ISignatureFile](T_Tessa_Platform_EDS_ISignatureFile.htm)
signingTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
signature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
digestAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
encryptionAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string) (Optional)
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)<[Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]>
#### Реализации
[ICAdESManager.MakeBesSignaturePkcs7Async(Byte[], ISignatureFile, DateTime,
Byte[], String, String,
CancellationToken)](M_Tessa_Platform_EDS_ICAdESManager_MakeBesSignaturePkcs7Async.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
