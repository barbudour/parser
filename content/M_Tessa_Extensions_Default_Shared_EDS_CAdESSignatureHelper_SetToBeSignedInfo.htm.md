# CAdESSignatureHelper.SetToBeSignedInfo - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public static void SetToBeSignedInfo(
    	CardRequest request,
    	byte[] certificate,
    	byte[] file,
    	DateTime signingTime,
    	string digestAlgorithmOid,
    	string encryptionAlgorithmOid
    )
VB __Копировать
     Public Shared Sub SetToBeSignedInfo ( 
    	request As CardRequest,
    	certificate As Byte(),
    	file As Byte(),
    	signingTime As DateTime,
    	digestAlgorithmOid As String,
    	encryptionAlgorithmOid As String
    )
C++ __Копировать
     public:
    static void SetToBeSignedInfo(
    	CardRequest^ request, 
    	array<unsigned char>^ certificate, 
    	array<unsigned char>^ file, 
    	DateTime signingTime, 
    	String^ digestAlgorithmOid, 
    	String^ encryptionAlgorithmOid
    )
F# __Копировать
     static member SetToBeSignedInfo : 
            request : CardRequest * 
            certificate : byte[] * 
            file : byte[] * 
            signingTime : DateTime * 
            digestAlgorithmOid : string * 
            encryptionAlgorithmOid : string -> unit 
#### Параметры
request [CardRequest](T_Tessa_Cards_CardRequest.htm)
certificate [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
file [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
signingTime [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
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
