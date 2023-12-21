# Tessa.Extensions.Default.Client.EDS - пространство имён
## __Классы
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm)|  
---|---  
[CryptoProEDSManager](T_Tessa_Extensions_Default_Client_EDS_CryptoProEDSManager.htm)|  
[Registrator](T_Tessa_Extensions_Default_Client_EDS_Registrator.htm)|
Регистратор должен выполняться после
[Registrator](T_Tessa_Extensions_Default_Shared_EDS_Registrator.htm), чтобы
переопределить регистрацию интерфейса без имени
[ICAdESManager](T_Tessa_Platform_EDS_ICAdESManager.htm).  
[ServiceEDSManagerForCAdES](T_Tessa_Extensions_Default_Client_EDS_ServiceEDSManagerForCAdES.htm)|
Выполняет подписание в отдельном хост-процессе с использованием Windows Crypto
API. Реализация [DecodeCertificateFromSignature(Byte[],
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_DecodeCertificateFromSignature.htm)
наследуется от
[DefaultEDSManager](T_Tessa_Extensions_Default_Shared_EDS_DefaultEDSManager.htm).
Для регистрации создайте [Registrator(Order = 2)], в методе RegisterUnity
укажите UnityContainer.RegisterType<ICAdESManager, ServiceEDSManager>(new
ContainerControlledLifetimeManager())  
[ServiceEDSManagerForCMS](T_Tessa_Extensions_Default_Client_EDS_ServiceEDSManagerForCMS.htm)|
Выполняет подписание в отдельном хост-процессе с использованием Windows Crypto
API. Реализация [DecodeCertificateFromSignature(Byte[],
CancellationToken)](M_Tessa_Platform_EDS_IEDSManager_DecodeCertificateFromSignature.htm)
наследуется от
[DefaultEDSManager](T_Tessa_Extensions_Default_Shared_EDS_DefaultEDSManager.htm).
Для регистрации создайте [Registrator(Order = 2)], в методе RegisterUnity
укажите UnityContainer.RegisterType<ICAdESManager, ServiceEDSManager>(new
ContainerControlledLifetimeManager())  
[SignatureSettingsStoreExtension](T_Tessa_Extensions_Default_Client_EDS_SignatureSettingsStoreExtension.htm)|  
[SignatureSettingsUIExtension](T_Tessa_Extensions_Default_Client_EDS_SignatureSettingsUIExtension.htm)|
