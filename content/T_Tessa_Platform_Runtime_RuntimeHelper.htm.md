# RuntimeHelper - класс
Вспомогательные методы для пространства имён Tessa.Platform.Runtime.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class RuntimeHelper
VB __Копировать
     Public NotInheritable Class RuntimeHelper
C++ __Копировать
     public ref class RuntimeHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type RuntimeHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RuntimeHelper
##  __Свойства
[ApplicationAliasOverride](P_Tessa_Platform_Runtime_RuntimeHelper_ApplicationAliasOverride.htm)|
Алиас приложения, используемый вместо алиаса, заданного в атрибуте сборки
[ApplicationAttribute](T_Tessa_Platform_Runtime_ApplicationAttribute.htm), или
null или пустая строка, если алиас приложения задаётся на основании этого
атрибута.  
---|---  
[AssemblyResolveActualLocationFunc](P_Tessa_Platform_Runtime_RuntimeHelper_AssemblyResolveActualLocationFunc.htm)|
Делегат, обеспечивающий алгоритм определения путей к файлу заданной сборки
вызовом
[GetActualLocationFolder(Assembly)](M_Tessa_Platform_PlatformExtensions_GetActualLocationFolder.htm).
Если делегат равен null (по умолчанию) или он возвращает null, то используется
стандартный алгоритм из метода
[GetLocationFileNameFromCodeBase(Assembly)](M_Tessa_Platform_PlatformExtensions_GetLocationFileNameFromCodeBase.htm),
определяющий местоположение сборки до того, как она могла быть скопирована
механизмом shadow copy.  
[ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm)|
Путь к папке, в которой выполняется поиск конфигурационных файлов, таких как
app.json и extensions.xml. Для поиска используется делегат
[ConfigRootPathFunc](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPathFunc.htm).
Если он не задан или вернул null, то поиск выполняется в переменной окружения
с именем
[ConfigRootPathEnvironmentVariable](F_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.  
[ConfigRootPathFunc](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPathFunc.htm)|
Делегат, вызываемый для определения папки с конфигурационными файлами
[ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm).
Вызывается один раз при запросе свойства
[ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm).
При изменении делегата свойство
[ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm)
будет вычислено повторно в момент обращения. Если делегат равен null (по
умолчанию) или вернул строку null, то будет использоваться определение папки
по умолчанию
[GetDefaultConfigRootPath()](M_Tessa_Platform_Runtime_RuntimeHelper_GetDefaultConfigRootPath.htm).
Не используйте свойства из файла конфигурации app.json, в т.ч. посредством
[ConfigurationManager](T_Tessa_Platform_ConfigurationManager.htm), потому что
для поиска app.json также используется свойство
[ConfigRootPath](P_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPath.htm), и
его использование приведёт к бесконечной рекурсии. Пример использования: () =>
Directory.GetCurrentDirectory(). Для WCF можно использовать: () =>
System.Web.Hosting.HostingEnvironment.ApplicationPhysicalPath.  
[MaxServerRecommendedParallelThreads](P_Tessa_Platform_Runtime_RuntimeHelper_MaxServerRecommendedParallelThreads.htm)|
Максимальное рекомендованное количество потоков для параллельных операций на
сервере. Зависит от настройки LimitMaxThreads в файле app.json. Значение можно
указать для
[MaxDegreeOfParallelism](https://learn.microsoft.com/dotnet/api/system.threading.tasks.paralleloptions.maxdegreeofparallelism#system-
threading-tasks-paralleloptions-maxdegreeofparallelism)  
[ServerRequestID](P_Tessa_Platform_Runtime_RuntimeHelper_ServerRequestID.htm)|
Уникальный идентификатор запроса на веб-сервере. Используется для
идентификации SQL-запросов в трассировке СУБД. Равен null, если действие не
выполняется в рамках запроса на веб-сервере. Значение передаётся между
потоками как AsyncLocal.  
[SwaggerDocIsEnabled](P_Tessa_Platform_Runtime_RuntimeHelper_SwaggerDocIsEnabled.htm)|
Признак того, что разрешён запрос по адресу /swagger для вывода документации
по API. По умолчанию false, т.е. проверка запрещена, если в конфигурационном
файле нет настройки SwaggerDocIsEnabled.  
[ThemeFolder](P_Tessa_Platform_Runtime_RuntimeHelper_ThemeFolder.htm)|  Путь к
папке с доступными темами оформления (относительно файлов приложения) или
null, если используется папка по умолчанию themes. Используйте совместно с
методом [GetExistentFolderPathList(String,
Assembly)](M_Tessa_Platform_Runtime_RuntimeHelper_GetExistentFolderPathList.htm).  
[UnknownServerPlatformVersion](P_Tessa_Platform_Runtime_RuntimeHelper_UnknownServerPlatformVersion.htm)|
Версия платформы по умолчанию на сервере, если сервер её не сообщил.
Соответствует последней версии платформы, которая не сообщала свою версию при
логине - это 3.5.0. Используйте это значение, если логин был выполнен и
свойство
[PlatformVersion](P_Tessa_Platform_Runtime_ISessionVersionHolder_PlatformVersion.htm)
вернуло null.  
## __Методы
[CheckCipherKey](M_Tessa_Platform_Runtime_RuntimeHelper_CheckCipherKey.htm)|
Проверяет на валидность ключ CipherKey, используемый для шифрования в системе.
Выбрасывает исключения, если ключ не является валидным.  
---|---  
[CheckSignatureKey](M_Tessa_Platform_Runtime_RuntimeHelper_CheckSignatureKey.htm)|
Проверяет на валидность ключ SignatureKey, используемый для подписи в системе.
Выбрасывает исключения, если ключ не является валидным.  
[ConvertKeyFromString](M_Tessa_Platform_Runtime_RuntimeHelper_ConvertKeyFromString.htm)|
Преобразует ключ SignatureKey или CipherKey из строки в формате base-64 в
массив байт. Возвращает null, если строка base64String является пустой строкой
или null. Подпись можно использовать, например, создав экземпляр класса
[SyncSignatureProvider](T_Tessa_Platform_SyncSignatureProvider.htm).  
[ConvertKeyToString](M_Tessa_Platform_Runtime_RuntimeHelper_ConvertKeyToString.htm)|
Преобразует ключ SignatureKey или CipherKey в строку в формате base-64. Ключ
может быть сгенерирован в т.ч. посредством методов
[GenerateSignatureKey()](M_Tessa_Platform_Runtime_RuntimeHelper_GenerateSignatureKey.htm)
или
[GenerateCipherKey()](M_Tessa_Platform_Runtime_RuntimeHelper_GenerateCipherKey.htm).  
[CreateWcfService<T>](M_Tessa_Platform_Runtime_RuntimeHelper_CreateWcfService__1.htm)|
Создаёт объект прокси для обращения к веб-сервису Tessa с заданными
параметрами.  
[ExecuteInImpersonationContext(String, String, Action<WindowsIdentity>,
String)](M_Tessa_Platform_Runtime_RuntimeHelper_ExecuteInImpersonationContext.htm)|
Выполняет заданное действие action в контексте имперсонализации, в которой
текущий
[WindowsIdentity](https://learn.microsoft.com/dotnet/api/system.security.principal.windowsidentity),
передаваемый также в параметре, определяется по заданным параметрам
пользователя.  
[ExecuteInImpersonationContext(String, String, String,
Action<WindowsIdentity>)](M_Tessa_Platform_Runtime_RuntimeHelper_ExecuteInImpersonationContext_1.htm)|
Выполняет заданное действие action в контексте имперсонализации, в которой
текущий
[WindowsIdentity](https://learn.microsoft.com/dotnet/api/system.security.principal.windowsidentity),
передаваемый также в параметре, определяется по заданным параметрам
пользователя.  
[FindConfigurationFilesWithKeys](M_Tessa_Platform_Runtime_RuntimeHelper_FindConfigurationFilesWithKeys.htm)|
Возвращает полные пути к конфигурационным файлам для сервисов, располагающихся
в заданной базовой папке, в которых могут располагаться ключи подписи
SignatureKey и ключи шифрования CipherKey. Учитываются файлы app.json. Также
возможно указать путь к конфигурационному файлу.  
[GenerateCipherKey](M_Tessa_Platform_Runtime_RuntimeHelper_GenerateCipherKey.htm)|
Генерирует ключ, который может использоваться для шифрования с использованием
алгоритмов AES. Размер ключа - 32 байт. Используется для шифрования информации
в базе данных, такой как закрытые ключи для шифрования файлов в локальных
папках пользователей. В системе метод используется для генерации ключа
шифрования CipherKey в файлах app.json (команда tadmin GetToken).  
[GenerateSignatureKey](M_Tessa_Platform_Runtime_RuntimeHelper_GenerateSignatureKey.htm)|
Генерирует ключ, который может использоваться для подписи. Размер ключа - 64
байт. Если это возможно, рекомендуется использовать стандартные средства
подписи [ISignatureProvider](T_Tessa_Platform_ISignatureProvider.htm), который
использует ключ, задаваемый для системы в целом. Например, ключ можно передать
в созданный экземпляр класса
[SyncSignatureProvider](T_Tessa_Platform_SyncSignatureProvider.htm), а затем
использовать для подписи или проверки подписи. В системе метод используется
для генерации ключа подписи токенов SignatureKey в файлах app.json (команда
tadmin GetToken) \- применяется для токена сессии и токена правил доступа;
также метод используется для генерации ключа PasswordKey для подписи пароля
пользователя PasswordHash по алгоритму HMACSHA256.  
[GetAbsolutePath](M_Tessa_Platform_Runtime_RuntimeHelper_GetAbsolutePath.htm)|
Получает абсолютный путь по пути path, который может быть относительным. Путь
вычисляется по исходному местоположению сборки entryAssembly. Если путь не
задан, то возвращает исходный путь path.  
[GetApplicationInfo](M_Tessa_Platform_Runtime_RuntimeHelper_GetApplicationInfo.htm)|
Возвращает информацию по сборке, полученную для атрибутов
[ApplicationAttribute](T_Tessa_Platform_Runtime_ApplicationAttribute.htm) и
[AssemblyTitleAttribute](https://learn.microsoft.com/dotnet/api/system.reflection.assemblytitleattribute).  
[GetApplicationInfoForDefaultApps](M_Tessa_Platform_Runtime_RuntimeHelper_GetApplicationInfoForDefaultApps.htm)|
Возвращает информацию по сборке для известных системе приложений: TessaClient,
TessaAdmin, TessaAppManager. Имя приложения name и его алиас alias будет
корректно определён только для известных приложений. Версия сборки
applicationVersion определяется для любых сборок .NET без их загрузки. Алиас
может быть переопределён в свойстве
[ApplicationAliasOverride](P_Tessa_Platform_Runtime_RuntimeHelper_ApplicationAliasOverride.htm),
тогда используется значение из свойства независимо от того, является ли
приложение известным. Если приложение было известным, то параметр knownApp
возвращает true.  
[GetBitmapFromIcon](M_Tessa_Platform_Runtime_RuntimeHelper_GetBitmapFromIcon.htm)|
Возвращает объект
[Bitmap](https://learn.microsoft.com/dotnet/api/system.drawing.bitmap) по
заданной иконке. Учитывает, что .NET может некорректно извлекать иконки
разрешения 256х256 и выше.  
[GetDefaultConfigRootPath](M_Tessa_Platform_Runtime_RuntimeHelper_GetDefaultConfigRootPath.htm)|
Алгоритм поиска по умолчанию для папки, в которой выполняется поиск
конфигурационных файлов, таких как app.json и extensions.xml. Поиск сначала
выполняется в переменной окружения с именем
[ConfigRootPathEnvironmentVariable](F_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm).
Если переменная равна точке ".", то используется текущая папка приложения
Directory.GetCurrentDirectory(). Если переменная не задана, то выполняется
поиск относительно папки со сборкой Tessa.dll.  
[GetExecutableFileName](M_Tessa_Platform_Runtime_RuntimeHelper_GetExecutableFileName.htm)|
Возвращает имя основного исполняемого файла или полный путь к нему, если
параметр fullPath указан как true. При невозможности получить имя файла или
путь будет возвращено null или выброшено исключение.  
[GetExistentFolderPathList](M_Tessa_Platform_Runtime_RuntimeHelper_GetExistentFolderPathList.htm)|
По пути к одной или нескольким папкам, который обычно задаётся в
конфигурационном файле, возвращает список абсолютных путей к тем из папок,
которые в действительности существуют. Метод не возвращает null.  
[GetIconBitmapStream](M_Tessa_Platform_Runtime_RuntimeHelper_GetIconBitmapStream.htm)|
Возвращает поток с данными иконки, который может использоваться для её
отображения в WPF в формате PNG. Возвращаемое значение не равно null.  
[GetInstanceNameOrDefault](M_Tessa_Platform_Runtime_RuntimeHelper_GetInstanceNameOrDefault.htm)|
Возвращает имя экземпляра instanceName или имя по умолчанию
[DefaultInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultInstanceName.htm),
если заданное имя instanceName является пустой строкой или null.  
[GetPasswordBytesToSign](M_Tessa_Platform_Runtime_RuntimeHelper_GetPasswordBytesToSign.htm)|
Возвращает массив байт, соответствующий заданной строке с паролем password,
или null, если переданная строка с паролем не содержит символов.  
[GetResourceTextFile](M_Tessa_Platform_Runtime_RuntimeHelper_GetResourceTextFile.htm)|
Возвращает содержимое текстового файла, включённого во встроенные ресурсы
сборки assembly и располагающегося по заданному абсолютному пути.  
[GetUtcOffset](M_Tessa_Platform_Runtime_RuntimeHelper_GetUtcOffset.htm)|
Возвращает текущее смещение относительно временной зоны UTC.  
[IsDefaultInstanceName](M_Tessa_Platform_Runtime_RuntimeHelper_IsDefaultInstanceName.htm)|
Возвращает признак того, что заданное имя экземпляра сервера является именем
по умолчанию. Такое имя может быть, например, пропущено в ссылках на карточки
и другие объекты системы.  
[OpenApplicationFolder](M_Tessa_Platform_Runtime_RuntimeHelper_OpenApplicationFolder.htm)|
Открывает папку приложения в Windows Explorer. Возвращает признак того, что
папка была успешно определена и открыта.  
[ParseBuildVersionString](M_Tessa_Platform_Runtime_RuntimeHelper_ParseBuildVersionString.htm)|
Выполняет разбор строки версии платформы на компоненты: MajorVersion \- первое
и второе число, разделённое через точку; MinorVersion \- третье число,
начинающееся на точку, или пустая строка, если третье число отсутствует (если
есть четвёртое число, то оно обычно здесь же); VersionSuffix \- суффикс версии
(такой как "beta" или "preview") или пустая строка, если версия считается
релизной.
Например, для строки version, равной "2.0.1 beta", возвращает:
MajorVersion="2.0", MinorVersion=".1", VersionSuffix="beta". Чтобы получить
объект [Version](https://learn.microsoft.com/dotnet/api/system.version),
объедените строки MajorVersion+MinorVersion.  
[ParseDomainAndUserNames](M_Tessa_Platform_Runtime_RuntimeHelper_ParseDomainAndUserNames.htm)|
Выполняет разбор имени учётной записи на имя домена и имя пользователя.  
[PrepareServicePointManagerIfNotPrepared](M_Tessa_Platform_Runtime_RuntimeHelper_PrepareServicePointManagerIfNotPrepared.htm)|
Подготавливает стандартный ServicePointManager для использования клиентской
части в Tessa, в т.ч. обеспечивает поддержку протоколов TLS (отключает SSLv3),
отключает валидацию SSL-сертификатов и настраивает пулинг для
ServicePointManager. Актуально только при запуске с подключением к службам WCF
(через ServicePointManager), настройки игнорируются для вызова веб-сервисов
через HttpClient и его аналоги. В текущей версии платформы включаются TLS 1.0,
1.1, 1.2 и 1.3 (с опциональным отключением младших версий 1.0 и 1.1). Метод
может быть вызван одновременно из нескольких потоков, а также несколько раз
подряд, при этом работает только первый вызов.  
[ReplaceKeyInConfigurationFoldersAsync](M_Tessa_Platform_Runtime_RuntimeHelper_ReplaceKeyInConfigurationFoldersAsync.htm)|
Выполняет замену ключа подписи SignatureKey или ключа шифрования CipherKey во
всех конфигурационных файлах сервисов, располагающихся в подпапках
относительно указанного базового пути. Доступна замена в конфигурационных
файлах формата app.json.  
[ResolveExactFilePath](M_Tessa_Platform_Runtime_RuntimeHelper_ResolveExactFilePath.htm)|
Возвращает путь к конкретному файлу, не содержащий символов масок * и ?, по
пути, который может ссылаться на несколько файлов, используя маски. При этом
возвращается первый файл по алфавиту.  
[TryExtractIconRecommendedSize(Byte[])](M_Tessa_Platform_Runtime_RuntimeHelper_TryExtractIconRecommendedSize.htm)|
Возвращает иконку рекомендуемых размеров или null, если такую иконку не
удалось извлечь.  
[TryExtractIconRecommendedSize(Icon)](M_Tessa_Platform_Runtime_RuntimeHelper_TryExtractIconRecommendedSize_1.htm)|
Возвращает иконку рекомендуемых размеров или null, если такую иконку не
удалось извлечь.  
[TryGetDefaultIconLocation](M_Tessa_Platform_Runtime_RuntimeHelper_TryGetDefaultIconLocation.htm)|
Возвращает путь к файлу с иконкой по умолчанию, которая может использоваться
для переопределения иконки приложения, или null, если путь не удалось
определить.  
[TryGetRecommendedIconDataFromIcoFileAsync](M_Tessa_Platform_Runtime_RuntimeHelper_TryGetRecommendedIconDataFromIcoFileAsync.htm)|
Возвращает данные для рекомендуемой иконки, полученной из заданного файла
формата .ICO, или null, если данные получить не удалось. Метод может выбросить
исключение.  
[TryReplaceKeyInConfigurationFileAsync](M_Tessa_Platform_Runtime_RuntimeHelper_TryReplaceKeyInConfigurationFileAsync.htm)|
Заменяет значение ключа подписи SignatureKey или ключа шифрования CipherKey,
используемых в Tessa. Доступна замена в конфигурационных файлах формата
app.json. Возвращает true, если ключ заменён; false, если ключ не заменён;
null, если конфигурационный файл должен игнорироваться при выводе сообщений.  
## __Поля
[ApplicationDefaultAlias](F_Tessa_Platform_Runtime_RuntimeHelper_ApplicationDefaultAlias.htm)|
Алиас приложения по умолчанию в случае, если у него отсутствует алиас,
полученный другим образом (в атрибуте сборки
[ApplicationAttribute](T_Tessa_Platform_Runtime_ApplicationAttribute.htm) или
в свойстве
[ApplicationAliasOverride](P_Tessa_Platform_Runtime_RuntimeHelper_ApplicationAliasOverride.htm)).  
---|---  
[CipherKeyName](F_Tessa_Platform_Runtime_RuntimeHelper_CipherKeyName.htm)|
Имя ключа шифрования CipherKey.  
[CipherKeySize](F_Tessa_Platform_Runtime_RuntimeHelper_CipherKeySize.htm)|
Размер в байтах ключа для шифрования информации CipherKey.  
[ConfigRootPathEnvironmentVariable](F_Tessa_Platform_Runtime_RuntimeHelper_ConfigRootPathEnvironmentVariable.htm)|
Имя переменной окружения, в которой выполняется поиск конфигурационных файлов,
таких как app.json и extensions.xml. Если переменная равна точке ".", то
используется текущая папка приложения Directory.GetCurrentDirectory(). Если
переменная не задана, то выполняется поиск относительно папки Tessa.dll
вызовом
[GetActualLocationFolder(Assembly)](M_Tessa_Platform_PlatformExtensions_GetActualLocationFolder.htm).  
[DefaultConfigurationString](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultConfigurationString.htm)|
Название строки подключения к базе данных Tessa.  
[DefaultInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultInstanceName.htm)|
Имя экземпляра сервера по умолчанию.  
[DefaultLegacyInstanceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultLegacyInstanceName.htm)|
Имя экземпляра, используемое для подключения к legacy-сервисам для сборок
платформы 2.x.  
[DefaultServiceName](F_Tessa_Platform_Runtime_RuntimeHelper_DefaultServiceName.htm)|
Имя веб-сервиса ASP.NET Core по умолчанию, содержащее все сервисы платформы.  
[EnableNotificationsLink](F_Tessa_Platform_Runtime_RuntimeHelper_EnableNotificationsLink.htm)|
Название действия на установку свойства
[NotificationsAreEnabled](P_Tessa_Platform_Runtime_IApplicationParameters_NotificationsAreEnabled.htm).
Действие принимает параметр "Value" как True или False.  
[InvalidLoginOrPasswordMessage](F_Tessa_Platform_Runtime_RuntimeHelper_InvalidLoginOrPasswordMessage.htm)|
Сообщение в исключениях при некорректном логине или пароле.  
[ServerRequestParameterName](F_Tessa_Platform_Runtime_RuntimeHelper_ServerRequestParameterName.htm)|
Имя параметра, добавляемого к запросам в БД для идентификации SQL-запросов,
принадлежащих одному и тому же запросу с клиента.  
[SessionHostIPMaxLength](F_Tessa_Platform_Runtime_RuntimeHelper_SessionHostIPMaxLength.htm)|
Максимальная длина для поля Session.HostIP.  
[SessionHostNameMaxLength](F_Tessa_Platform_Runtime_RuntimeHelper_SessionHostNameMaxLength.htm)|
Максимальная длина для поля Session.HostName.  
[SessionOSNameMaxLength](F_Tessa_Platform_Runtime_RuntimeHelper_SessionOSNameMaxLength.htm)|
Максимальная длина для поля Session.OSName.  
[SessionUserAgentMaxLength](F_Tessa_Platform_Runtime_RuntimeHelper_SessionUserAgentMaxLength.htm)|
Максимальная длина для поля Session.UserAgent.  
[SignatureKeyName](F_Tessa_Platform_Runtime_RuntimeHelper_SignatureKeyName.htm)|
Имя ключа подписи SignatureKey.  
[SignatureKeySize](F_Tessa_Platform_Runtime_RuntimeHelper_SignatureKeySize.htm)|
Размер в байтах ключа для подписи токенов SignatureKey.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
