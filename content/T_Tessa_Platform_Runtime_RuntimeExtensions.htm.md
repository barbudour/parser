# RuntimeExtensions - класс
Методы-расширения для пространства имён Tessa.Platform.Runtime.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RuntimeExtensions
VB __Копировать
    <ExtensionAttribute>
    Public NotInheritable Class RuntimeExtensions
C++ __Копировать
    [ExtensionAttribute]
    public ref class RuntimeExtensions abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    [<ExtensionAttribute>]
    type RuntimeExtensions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RuntimeExtensions
##  __Методы
[CheckSealed](M_Tessa_Platform_Runtime_RuntimeExtensions_CheckSealed.htm)|
Выбрасывает исключение
[ConfigurationSealedException](T_Tessa_Platform_Runtime_ConfigurationSealedException.htm),
если система находится в режиме защиты от изменений в конфигурации
[Sealed](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
---|---  
[CheckStrictSecurity](M_Tessa_Platform_Runtime_RuntimeExtensions_CheckStrictSecurity.htm)|
Выбрасывает исключение
[ConfigurationStrictSecurityException](T_Tessa_Platform_Runtime_ConfigurationStrictSecurityException.htm),
если система находится в режиме защиты повышенной безопасности в конфигурации
[StrictSecurity](T_Tessa_Platform_Runtime_ConfigurationFlags.htm).  
[CreateNestedSessionToken](M_Tessa_Platform_Runtime_RuntimeExtensions_CreateNestedSessionToken.htm)|
Создаёт токен [SessionToken](T_Tessa_Platform_Runtime_SessionToken.htm) для
сотрудника с заданными настройками, но наследующий информацию по серверу и
текущей культуре из текущей сессии session. Используйте возвращённый токен в
объекте [SessionContext](T_Tessa_Platform_Runtime_SessionContext.htm), который
создаётся для выполнения действий в пределах уже существующей сессии,
например, со стороны веб-сервисов.  
[CreateWcfService<T>(IUnityContainer, String, HttpClientCredentialType,
String, Action<ChannelFactory<T>>, Func<SessionServiceAttribute,
Binding>)](M_Tessa_Platform_Runtime_RuntimeExtensions_CreateWcfService__1.htm)|
Создаёт прокси для обращения к веб-сервису T с атрибутом
[SessionServiceAttribute](T_Tessa_Platform_Runtime_SessionServiceAttribute.htm).  
[CreateWcfService<T>(IUnityContainer, IConnectionSettings, String,
HttpClientCredentialType, String, Action<ChannelFactory<T>>,
Func<SessionServiceAttribute,
Binding>)](M_Tessa_Platform_Runtime_RuntimeExtensions_CreateWcfService__1_1.htm)|
Создаёт прокси для обращения к веб-сервису T с атрибутом
[SessionServiceAttribute](T_Tessa_Platform_Runtime_SessionServiceAttribute.htm).  
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>(IExtensionExecutor<TExtension>,
Expression<ExtensionMethodReferenceAsync<TExtension, TExtensionContext>>,
TExtensionContext, ILogger, Func<IExtensionStrategyContext, ValueTask>,
Boolean)](M_Tessa_Platform_Runtime_RuntimeExtensions_ExecuteWithExceptionCheckAsync__2.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они логируются объектом Logger.  
[ExecuteWithExceptionCheckAsync<TExtension,
TExtensionContext>(IExtensionExecutor<TExtension>,
Expression<ExtensionMethodReferenceAsync<TExtension, TExtensionContext>>,
TExtensionContext, IMessageProvider, Func<IExtensionStrategyContext,
ValueTask>,
Boolean)](M_Tessa_Platform_Runtime_RuntimeExtensions_ExecuteWithExceptionCheckAsync__2_1.htm)|
Выполняет заданный метод расширений с обработкой исключений, при возникновении
которых они обрабатываются объектом
[IMessageProvider](T_Tessa_Platform_Runtime_IMessageProvider.htm), например,
логируются и выводятся пользователю.  
[FinalizeSessionsOnClient](M_Tessa_Platform_Runtime_RuntimeExtensions_FinalizeSessionsOnClient.htm)|
Выполняет финализацию для процесса регистрации сессий на стороне клиента.
Метод должен быть вызван после того, как все регистрации в контейнере будут
завершены.  
[GenerateSignature](M_Tessa_Platform_Runtime_RuntimeExtensions_GenerateSignature.htm)|
Создаёт подпись для заданных свойств, связанных с сессией.  
[GetLicenseCount](M_Tessa_Platform_Runtime_RuntimeExtensions_GetLicenseCount.htm)|
Возвращает количество доступных лицензий для заданного типа licenseType. Для
типа [Unspecified](T_Tessa_Platform_Runtime_SessionLicenseType.htm)
возвращается -1.  
[GetNameWithBitness](M_Tessa_Platform_Runtime_RuntimeExtensions_GetNameWithBitness.htm)|
Возвращает имя приложения с суффиксом, указывающим на его 64-битность (если
процесс 64-битный).  
[GetSessionExceptionCode](M_Tessa_Platform_Runtime_RuntimeExtensions_GetSessionExceptionCode.htm)|
Возвращает код исключения, выброшенного на сервере как
[SessionException](T_Tessa_Platform_Runtime_SessionException.htm), или
[Unknown](T_Tessa_Platform_Runtime_SessionExceptionCode.htm), если код
исключения получить не удалось.  
[IsAdministrator](M_Tessa_Platform_Runtime_RuntimeExtensions_IsAdministrator.htm)|
Возвращает признак того, что пользователь является администратором системы.  
[IsConcurrent](M_Tessa_Platform_Runtime_RuntimeExtensions_IsConcurrent.htm)|
Возвращает признак того, что лицензия заданного типа является конкурентной.  
[IsDesktopClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsDesktopClient.htm)|
Возвращает признак того, что сессия была открыта с десктопного клиента (т.е. с
"толстого" клиента). Это могут быть приложения TessaAdmin, TessaClient,
консольный tadmin, интеграционный веб-сервис и др.  
[IsExceptionCritical](M_Tessa_Platform_Runtime_RuntimeExtensions_IsExceptionCritical.htm)|
Возвращает признак того, что указанное исключение относится в разряд
критических и должно привести к завершению приложения.  
[IsInvalidLoginOrPassword](M_Tessa_Platform_Runtime_RuntimeExtensions_IsInvalidLoginOrPassword.htm)|
Возвращает признак того, что заданный код ошибки связан с некорректным логином
или паролем.  
[IsLoginHiddenException](M_Tessa_Platform_Runtime_RuntimeExtensions_IsLoginHiddenException.htm)|
Возвращает признак того, что исключение не отображается пользователю, когда
оно возникло при входе в систему. Например, пользователь не входит в домен.  
[IsNotWebOrDesktopClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsNotWebOrDesktopClient.htm)|
Возвращает признак того, что сессия была открыта не с десктопного клиента и не
с Web-клиента. Обычно это плагины Chronos, интеграционные веб-сервисы с
собственной авторизацией и другие приложения.  
[IsPersonal](M_Tessa_Platform_Runtime_RuntimeExtensions_IsPersonal.htm)|
Возвращает признак того, что лицензия заданного типа является персональной.  
[IsRegular](M_Tessa_Platform_Runtime_RuntimeExtensions_IsRegular.htm)|
Возвращает признак того, что пользователь является обычным пользователем.  
[IsUnauthorizedWebException](M_Tessa_Platform_Runtime_RuntimeExtensions_IsUnauthorizedWebException.htm)|
Возвращает признак того, что исключение является ошибкой с кодом ошибки 401:
[Unauthorized](https://learn.microsoft.com/dotnet/api/system.net.httpstatuscode).
Обычно такое исключение происходит при неудачной авторизации Windows.
Учитывает агрегирование асинхронных исключений.  
[IsWebClient](M_Tessa_Platform_Runtime_RuntimeExtensions_IsWebClient.htm)|
Возвращает признак того, что сессия была открыта с Web-клиента (т.е. с
"лёгкого" клиента). Это или Web-клиент Tessa, или интеграция через Web API.  
[RegisterApplicationExtensionTypes](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationExtensionTypes.htm)|
Выполняет регистрацию стандартных типов расширений для API инициализации на
клиенте.  
[RegisterApplicationsTraceListeners](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationsTraceListeners.htm)|
Выполняет регистрацию объектов, отслеживающих события, происходящие при
выполнении расширений на инициализацию приложения со стороны сервера, и
записывающие результат выполнения в
[ValidationResult](T_Tessa_Platform_Validation_ValidationResult.htm) как
информационное сообщение. Это полезно при отладке расширений, но сильно
нагружает любое взаимодействие с плитками, поэтому рекомендуется не выполнять
такую регистрацию в среде, с которой работают конечные пользователи.  
[RegisterConnectionSettingsFromConfiguration](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterConnectionSettingsFromConfiguration.htm)|
Регистрирует зависимость
[IConnectionSettings](T_Tessa_Platform_Runtime_IConnectionSettings.htm) со
значениями, полученными из менеджера конфигурации
[IConfigurationManager](T_Tessa_Platform_IConfigurationManager.htm), также
зарегистрированного в Unity (он может быть зарегистрирован вызовом
[RegisterPlatformSharedDependencies(IUnityContainer)](M_Tessa_Platform_PlatformExtensions_RegisterPlatformSharedDependencies.htm)).
Обычно конфигурация расположена в файле app.json.  
[RegisterExtensionTracingOnServer](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterExtensionTracingOnServer.htm)|
Регистрирует зависимости, связанные с трассировкой расширений со стороны
сервера.  
[RegisterSessionsOnClient](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterSessionsOnClient.htm)|
Выполняет регистрацию сессии на стороне клиента по токену Tessa, а также
регистрирует объект
[IApplicationDescriptor](T_Tessa_Platform_Runtime_IApplicationDescriptor.htm)
и некоторые другие зависимости для обеспечения работы сессии, в т.ч.
[RegisterWebProxyFactory(IUnityContainer)](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterWebProxyFactory.htm).
После выполнения всех регистраций в контейнере рекомендуется вызвать метод
[FinalizeSessionsOnClient(IUnityContainer)](M_Tessa_Platform_Runtime_RuntimeExtensions_FinalizeSessionsOnClient.htm).  
[RegisterSessionsOnServer](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterSessionsOnServer.htm)|
Регистрирует реализацию сессий на сервере.  
[RegisterWcfService<T>(IUnityContainer,
String)](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterWcfService__1.htm)|
Регистрирует прокси для обращения к веб-сервису T с атрибутом
[SessionServiceAttribute](T_Tessa_Platform_Runtime_SessionServiceAttribute.htm).  
[RegisterWcfService<T>(IUnityContainer, IConnectionSettings,
String)](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterWcfService__1_1.htm)|
Регистрирует прокси для обращения к веб-сервису T с атрибутом
[SessionServiceAttribute](T_Tessa_Platform_Runtime_SessionServiceAttribute.htm).  
[RegisterWebProxyFactory](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterWebProxyFactory.htm)|
Выполняет регистрацию фабрики прокси-объектов
[IWebProxyFactory](T_Tessa_Platform_Runtime_IWebProxyFactory.htm) и некоторых
её зависимостей.  
[RemoveApplicationsTraceListeners](M_Tessa_Platform_Runtime_RuntimeExtensions_RemoveApplicationsTraceListeners.htm)|
Удаляет объекты, зарегистрированные методом
[RegisterApplicationsTraceListeners(IExtensionContainer,
ExtensionTraceListenerType,
Nullable<Int64>)](M_Tessa_Platform_Runtime_RuntimeExtensions_RegisterApplicationsTraceListeners.htm).
Частая регистрация с последующим удалением объектов значительно нагружает
память и CPU.  
[ReportErrorSafeAsync](M_Tessa_Platform_Runtime_RuntimeExtensions_ReportErrorSafeAsync.htm)|
Сообщает об ошибке с заданными параметрами и с необязательным дополнительным
описанием, в т.ч. с файлами. Для ошибки создаётся карточка с детальным
описанием и с заданным идентификатором, в которой можно выполнять поиск по
категории и тексту. Если при отправке ошибки возникло любое исключение, то оно
поглощается и заносится в лог [Error](F_Tessa_Platform_TessaLoggers_Error.htm)
Метод возвращает идентификатор фактически созданной ошибки или null, если при
отправке ошибки возникло исключение.  
[SetExtensionTracingFromSettingsOnServer](M_Tessa_Platform_Runtime_RuntimeExtensions_SetExtensionTracingFromSettingsOnServer.htm)|
Настраивает зависимости, связанные с трассировкой расширений на карточки, по
информации из настроек сервера
[ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm),
зарегистрированных в контейнере.  
[ToFaultException](M_Tessa_Platform_Runtime_RuntimeExtensions_ToFaultException.htm)|
Преобразует исключение
[SessionException](T_Tessa_Platform_Runtime_SessionException.htm) в исключение
[FaultException](https://learn.microsoft.com/dotnet/api/system.servicemodel.faultexception)
с корректной информацией по коду ошибки.  
[VerifySignature(ISignatureProvider,
ISessionToken)](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature_1.htm)|
Выполняет проверку подписи для заданного токена
[ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm) и возвращает
признак того, что подпись корректна.  
[VerifySignature(ISignatureProvider, Guid, String, String,
String)](M_Tessa_Platform_Runtime_RuntimeExtensions_VerifySignature.htm)|
Выполняет проверку подписи для заданных свойств, связанных с сессией, и
возвращает признак того, что подпись корректна.  
[WhenAnyApplication](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenAnyApplication.htm)|
Регистрирует политику фильтрации выполнения методов расширений по любым типам
приложений. Используйте для замещения политики, назначенной посредством метода
[WhenApplications(IExtensionPolicyContainer,
Guid[])](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplications.htm). Для
того, чтобы политика использовалась, требуется зарегистрировать политику
[ApplicationExtensionFilterPolicy](T_Tessa_Platform_Runtime_ApplicationExtensionFilterPolicy.htm).  
[WhenApplicationFunc](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplicationFunc.htm)|
Регистрирует политику фильтрации выполнения методов расширений
[IApplicationExtension](T_Tessa_Platform_Runtime_IApplicationExtension.htm) в
соответствии с функцией isAllowedFunc, которая проверяет контекст расширений.
Если зарегистрировано несколько политик, то должны выполняться все из них.  
[WhenApplications](M_Tessa_Platform_Runtime_RuntimeExtensions_WhenApplications.htm)|
Регистрирует политику фильтрации выполнения методов расширений по
идентификатору типа приложения, который входит в заданный список
идентификаторов. Для того, чтобы политика использовалась, требуется
зарегистрировать политику
[ApplicationExtensionFilterPolicy](T_Tessa_Platform_Runtime_ApplicationExtensionFilterPolicy.htm).
Регистрация добавляет значение к списку приложений, а не переопределяет его.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
