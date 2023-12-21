# CAdESManager.DecodeCertificateFromSignature - метод
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.EDS](N_Tessa_Extensions_Default_Shared_EDS.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public virtual (IEDSCertificate certificate, string errorText) DecodeCertificateFromSignature(
    	byte[] encodedSignature,
    	CancellationToken cancellationToken = default
    )
VB __Копировать
     Public Overridable Function DecodeCertificateFromSignature ( 
    	encodedSignature As Byte(),
    	Optional cancellationToken As CancellationToken = Nothing
    ) As (certificate As IEDSCertificate, errorText As String)
C++ __Копировать
     public:
    virtual ValueTuple<IEDSCertificate^, String^> DecodeCertificateFromSignature(
    	array<unsigned char>^ encodedSignature, 
    	CancellationToken cancellationToken = CancellationToken()
    )
F# __Копировать
     abstract DecodeCertificateFromSignature : 
            encodedSignature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTuple<IEDSCertificate, string> 
    override DecodeCertificateFromSignature : 
            encodedSignature : byte[] * 
            ?cancellationToken : CancellationToken 
    (* Defaults:
            let _cancellationToken = defaultArg cancellationToken new CancellationToken()
    *)
    -> ValueTuple<IEDSCertificate, string> 
#### Параметры
encodedSignature [Byte](https://learn.microsoft.com/dotnet/api/system.byte)[]
cancellationToken
[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)
(Optional)
#### Возвращаемое значение
[ValueTuple](https://learn.microsoft.com/dotnet/api/system.valuetuple-2)<[IEDSCertificate](T_Tessa_Platform_EDS_IEDSCertificate.htm),
[String](https://learn.microsoft.com/dotnet/api/system.string)>
#### Реализации
[IEDSManager.DecodeCertificateFromSignature(Byte[],
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_DecodeCertificateFromSignature.htm)  
##  __См. также
#### Ссылки
[CAdESManager - ](T_Tessa_Extensions_Default_Shared_EDS_CAdESManager.htm)
[Tessa.Extensions.Default.Shared.EDS - пространство
имён](N_Tessa_Extensions_Default_Shared_EDS.htm)
