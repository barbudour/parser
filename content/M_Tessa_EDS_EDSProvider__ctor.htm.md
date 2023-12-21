# EDSProvider - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.EDS](N_Tessa_EDS.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public EDSProvider(
    	ICAdESServiceSettings signatureSettings,
    	ICardCache cardCache,
    	Func<ICAdESServiceSettings, IDocumentSignatureService> getCAdESServiceFunc
    )
VB __Копировать
     Public Sub New ( 
    	signatureSettings As ICAdESServiceSettings,
    	cardCache As ICardCache,
    	getCAdESServiceFunc As Func(Of ICAdESServiceSettings, IDocumentSignatureService)
    )
C++ __Копировать
     public:
    EDSProvider(
    	ICAdESServiceSettings^ signatureSettings, 
    	ICardCache^ cardCache, 
    	Func<ICAdESServiceSettings^, IDocumentSignatureService^>^ getCAdESServiceFunc
    )
F# __Копировать
     new : 
            signatureSettings : ICAdESServiceSettings * 
            cardCache : ICardCache * 
            getCAdESServiceFunc : Func<ICAdESServiceSettings, IDocumentSignatureService> -> EDSProvider
#### Параметры
signatureSettings ICAdESServiceSettings
    Настройки подписания и проверки подписи, используемые по умолчанию.
cardCache [ICardCache](T_Tessa_Cards_Caching_ICardCache.htm)
     Кэш карточек-синглтонов, используемый по умолчанию для получения карточки настроек ЭП [SignatureSettingsType](F_Tessa_Platform_EDS_SignatureHelper_SignatureSettingsType.htm). 
getCAdESServiceFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<ICAdESServiceSettings,
IDocumentSignatureService>
     Возвращает сервис взаимодействия с криптопровайдерами IDocumentSignatureService для указанных настроек ICAdESServiceSettings. 
## __См. также
#### Ссылки
[EDSProvider - ](T_Tessa_EDS_EDSProvider.htm)
[Tessa.EDS - пространство имён](N_Tessa_EDS.htm)
