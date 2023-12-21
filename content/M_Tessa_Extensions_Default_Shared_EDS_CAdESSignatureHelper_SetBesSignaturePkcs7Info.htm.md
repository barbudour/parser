# CAdESSignatureHelper.SetBesSignaturePkcs7Info - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetBesSignaturePkcs7Info(
    	CardRequest request,
    	byte[] certificate,
    	byte[] file,
    	DateTime signingTime,
    	byte[] signature,
    	string digestAlgorithmOid,
    	string encryptionAlgorithmOid
    )
VB __Копировать
     Public Shared Sub SetBesSignaturePkcs7Info ( 
    	request As CardRequest,
    	certificate As Byte(),
    	file As Byte(),
    	signingTime As DateTime,
    	signature As Byte(),
    	digestAlgorithmOid As String,
    	encryptionAlgorithmOid As String
    )
C++ __Копировать
     public:
    static void SetBesSignaturePkcs7Info(
    	CardRequest^ request, 
    	array<unsigned char>^ certificate, 
    	array<unsigned char>^ file, 
    	DateTime signingTime, 
    	array<unsigned char>^ signature, 
    	String^ digestAlgorithmOid, 
    	String^ encryptionAlgorithmOid
    )
F# __Копировать
     static member SetBesSignaturePkcs7Info : 
            request : CardRequest * 
            certificate : byte[] * 
            file : byte[] * 
            signingTime : DateTime * 
            signature : byte[] * 
            digestAlgorithmOid : string * 
            encryptionAlgorithmOid : string -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
signingTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
signature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
digestAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string)
encryptionAlgorithmOid
[String](https://learn.microsoft.com/dotnet/api/system.string)
## __См. также
#### Ссылки
[CAdESSignatureHelper -
](T_Tessa_Extensions_Default_Shared_EDS_CAdESSignatureHelper.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
