# ApplicationPipeService - конструктор
Инициализирует новый экземпляр класса
[ApplicationPipeService](T_Tessa_Applications_Pipes_ApplicationPipeService.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Applications.Pipes](N_Tessa_Applications_Pipes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationPipeService(
    	IConnectionSettings connectionSettings,
    	ISessionTokenHolder tokenHolder,
    	Func<IApplicationServiceLegacy> serviceLegacyFunc
    )
VB __Копировать
     Public Sub New ( 
    	connectionSettings As IConnectionSettings,
    	tokenHolder As ISessionTokenHolder,
    	serviceLegacyFunc As Func(Of IApplicationServiceLegacy)
    )
C++ __Копировать
     public:
    ApplicationPipeService(
    	IConnectionSettings^ connectionSettings, 
    	ISessionTokenHolder^ tokenHolder, 
    	Func<IApplicationServiceLegacy^>^ serviceLegacyFunc
    )
F# __Копировать
     new : 
            connectionSettings : IConnectionSettings * 
            tokenHolder : ISessionTokenHolder * 
            serviceLegacyFunc : Func<IApplicationServiceLegacy> -> ApplicationPipeService
#### Параметры
connectionSettings
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm)
tokenHolder
[ISessionTokenHolder](T_Tessa_Platform_Runtime_ISessionTokenHolder.htm)
serviceLegacyFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[IApplicationServiceLegacy](T_Tessa_Applications_Services_TessaServer_IApplicationServiceLegacy.htm)>
## __См. также
#### Ссылки
[ApplicationPipeService -
](T_Tessa_Applications_Pipes_ApplicationPipeService.htm)
[Tessa.Applications.Pipes - пространство имён](N_Tessa_Applications_Pipes.htm)
