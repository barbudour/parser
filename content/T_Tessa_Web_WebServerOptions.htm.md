# WebServerOptions - класс
Настройки веб-сервера TESSA, используемого для Kestrel. Обычно содержатся в
файле app.json и доступны по свойству
[Configuration](P_Tessa_Web_WebServerOptions_Configuration.htm). Конструктор
по умолчанию создаёт объект, в котором все свойства имеют рекомендованные
значения по умолчанию.
## __Definition
 **Пространство имён:** [Tessa.Web](N_Tessa_Web.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class WebServerOptions
VB __Копировать
     Public NotInheritable Class WebServerOptions
C++ __Копировать
     public ref class WebServerOptions sealed
F# __Копировать
     [<SealedAttribute>]
    type WebServerOptions = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WebServerOptions
##  __Конструкторы
[WebServerOptions](M_Tessa_Web_WebServerOptions__ctor.htm)| Инициализирует
новый экземпляр класса WebServerOptions  
---|---  
##  __Свойства
[CertificateFile](P_Tessa_Web_WebServerOptions_CertificateFile.htm)|  Путь к
файлу сертификата для соединения по HTTPS или null (по умолчанию), если
сертификат не загружается из файла. Загрузка сертификата из файла более
приоритетна, чем его загрузка из хранилища.  
---|---  
[CertificateKeyFile](P_Tessa_Web_WebServerOptions_CertificateKeyFile.htm)|
Путь к файлу приватного ключа сертификата
[CertificateFile](P_Tessa_Web_WebServerOptions_CertificateFile.htm) или null
(по умолчанию), если приватный ключ не требуется или сертификат не загружается
из файла.  
[CertificatePassword](P_Tessa_Web_WebServerOptions_CertificatePassword.htm)|
Пароль для сертификата в файле
[CertificateFile](P_Tessa_Web_WebServerOptions_CertificateFile.htm) или null
(по умолчанию), если пароль не требуется или сертификат не загружается из
файла. Загрузка сертификата из файла более приоритетна, чем его загрузка из
хранилища.  
[CertificateStoreLocation](P_Tessa_Web_WebServerOptions_CertificateStoreLocation.htm)|
Местоположение хранилища сертификатов, из которого загружается сертификат для
соединения по HTTPS, или null (по умолчанию), если сертификат не загружается
из хранилища. Загрузка сертификата из хранилища менее приоритетна, чем его
загрузка из файла.  
[CertificateStoreName](P_Tessa_Web_WebServerOptions_CertificateStoreName.htm)|
Имя хранилища сертификатов, из которого загружается сертификат для соединения
по HTTPS, или null (по умолчанию), если сертификат не загружается из
хранилища. Загрузка сертификата из хранилища менее приоритетна, чем его
загрузка из файла.  
[CertificateStoreSubject](P_Tessa_Web_WebServerOptions_CertificateStoreSubject.htm)|
Поле "Subject" сертификата из хранилища, поиск которого выполняется. Укажите
null (не рекомендуется), чтобы использовался первый доступный сертификат в
хранилище. По умолчанию указана строка "localhost". Для загрузки из хранилища
также должны быть установлены свойства
[CertificateStoreName](P_Tessa_Web_WebServerOptions_CertificateStoreName.htm)
и
[CertificateStoreLocation](P_Tessa_Web_WebServerOptions_CertificateStoreLocation.htm).  
[Configuration](P_Tessa_Web_WebServerOptions_Configuration.htm)|  Объект
настроек, загруженный из конфигурации app.json.  
[DataProtectionCertificateFile](P_Tessa_Web_WebServerOptions_DataProtectionCertificateFile.htm)|
Путь к файлу сертификата для шифрования сохраняемых ключей "Data Protection",
используемых сервером Kestrel, или null (по умолчанию), если ключи шифруются
средствами текущей учётной записи (на Windows) или не шифруются (на Linux, не
рекомендуется). Настройка игнорируется, если не указан путь
[DataProtectionKeysPath](P_Tessa_Web_WebServerOptions_DataProtectionKeysPath.htm).  
[DataProtectionCertificateKeyFile](P_Tessa_Web_WebServerOptions_DataProtectionCertificateKeyFile.htm)|
Путь к файлу приватного ключа сертификата
[DataProtectionCertificateFile](P_Tessa_Web_WebServerOptions_DataProtectionCertificateFile.htm)
для шифрования сохраняемых ключей "Data Protection", используемых сервером
Kestrel, или null (по умолчанию), если приватный ключ не требуется или
сертификат не загружается из файла. Настройка игнорируется, если не указан
путь
[DataProtectionKeysPath](P_Tessa_Web_WebServerOptions_DataProtectionKeysPath.htm).  
[DataProtectionCertificatePassword](P_Tessa_Web_WebServerOptions_DataProtectionCertificatePassword.htm)|
Пароль для файла сертификата
[DataProtectionCertificateFile](P_Tessa_Web_WebServerOptions_DataProtectionCertificateFile.htm)
для шифрования сохраняемых ключей "Data Protection", используемых сервером
Kestrel, или null (по умолчанию), если пароль не требуется или сертификат не
загружается из файла. Настройка игнорируется, если не указан путь
[DataProtectionKeysPath](P_Tessa_Web_WebServerOptions_DataProtectionKeysPath.htm).  
[DataProtectionKeysPath](P_Tessa_Web_WebServerOptions_DataProtectionKeysPath.htm)|
Путь для сохранения ключей "Data Protection", используемых сервером Kestrel.
Если указаны null или пустая строка, то по умолчанию используется папка внутри
профиля %LocalAppData%. При запуске в контейнере Docker укажите путь к папке,
которая включена в volume Docker, чтобы содержимое папки сохранялось между
запусками приложения. В остальных случаях можно оставить путь пустым.
Подробнее этот механизм описан в MSDN: https://docs.microsoft.com/en-
us/aspnet/core/security/data-
protection/configuration/overview?view=aspnetcore-3.1  
[EnforceTls12](P_Tessa_Web_WebServerOptions_EnforceTls12.htm)|  Признак того,
что сервер будет разрешать только подключения от клиентов по протоколам TLS
1.2 и TLS 1.3. Если указано false, то также разрешается подключение по TLS 1.0
и TLS 1.1. Если указать true, то могут возникнуть проблемы с подключениями
клиентов со старыми версиями Windows или с установкой на сервер со старой
версией Windows (Windows 7, Windows 8, Windows Server 2008R2 Windows Server
2012) - на этих версиях ОС поддержку TLS 1.2 можно включить установкой
обновления Windows и модификацией реестра - обратитесь к MSDN. Установите true
только в том случае, если вы уверены, что таких клиентов не будет, или если их
не должно быть по политике безопасности вашей организации. По умолчанию false.  
[HstsMaxAgeDays](P_Tessa_Web_WebServerOptions_HstsMaxAgeDays.htm)|  Количество
дней, передаваемых в заголовке HSTS, если указан режим
[HttpsRedirect](P_Tessa_Web_WebServerOptions_HttpsRedirect.htm), равный
[Hsts](T_Tessa_Web_HttpsRedirectMode.htm). На указанное количество дней
браузер запоминает, что к указанному домену и его поддоменам следуем
обращаться только по протоколу HTTPS, даже если пользователь указал HTTP. По
умолчанию равно 365.  
[Http2Disabled](P_Tessa_Web_WebServerOptions_Http2Disabled.htm)|  Признак
того, что на сервере отключается поддержка протокола HTTP/2, при этом будет
использован только протокол HTTP 1.1. Укажите эту настройку, если при открытии
веб-приложения в браузере возникает ошибка
ERR_HTTP2_INADEQUATE_TRANSPORT_SECURITY. По умолчанию false.  
[HttpsRedirect](P_Tessa_Web_WebServerOptions_HttpsRedirect.htm)|  Режим
редиректа с протокола HTTP на endpoint с протоколом HTTPS. По умолчанию
[Disabled](T_Tessa_Web_HttpsRedirectMode.htm).  
[HttpsRedirectPort](P_Tessa_Web_WebServerOptions_HttpsRedirectPort.htm)|
Порт, по которому выполняется редирект с протокола HTTP на endpoint с
протоколом HTTPS, если такой редирект доступен согласно настройке
[HttpsRedirect](P_Tessa_Web_WebServerOptions_HttpsRedirect.htm). Укажите null
(по умолчанию), чтобы автоматически выбрать порт в соответствии со списком
прослушиваемых адресов (должен быть только один адрес, прослушиваемый по
протоколу https, иначе редирект не будет выполняться).  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromConfiguration(Dictionary<String,
Object>)](M_Tessa_Web_WebServerOptions_FromConfiguration.htm)|  Создаёт объект
настроек по заданному объекту с хеш-таблицей. По ключу "WebServer" в этой хеш-
таблице должны быть настройки. Имена настроек соотносятся с именами свойств
текущего объекта.  
[FromConfiguration(IConfigurationManager)](M_Tessa_Web_WebServerOptions_FromConfiguration_1.htm)|
Создаёт объект настроек по заданному объекту конфигурации. В нём по свойству
configurationManager.Configuration.Settings доступна хеш-таблица, в которой
есть ключ "WebServer", содержащий настройки. Имена настроек соотносятся с
именами свойств текущего объекта.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetFrom](M_Tessa_Web_WebServerOptions_SetFrom.htm)|  Устанавливает свойства
класса в соответствии с переданным объектом.  
[ToString](M_Tessa_Web_WebServerOptions_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Web - пространство имён](N_Tessa_Web.htm)
