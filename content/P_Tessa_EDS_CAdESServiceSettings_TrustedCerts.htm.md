# CAdESServiceSettings.TrustedCerts - свойство
##  __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public IList<X509Certificate> TrustedCerts { get; }
VB __Копировать
     Public ReadOnly Property TrustedCerts As IList(Of X509Certificate)
    	Get
C++ __Копировать
     public:
    virtual property IList<X509Certificate^>^ TrustedCerts {
    	IList<X509Certificate^>^ get () sealed;
    }
F# __Копировать
     abstract TrustedCerts : IList<X509Certificate> with get
    override TrustedCerts : IList<X509Certificate> with get
#### Значение свойства
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<X509Certificate>
#### Реализации
ICertificateSourceSettings.TrustedCerts  
##  __См. также
#### Ссылки
[CAdESServiceSettings - ](T_Tessa_EDS_CAdESServiceSettings.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
