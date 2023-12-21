# ITessaServerSettings - интерфейс
Настройки TESSA на сервере, которые выносятся в конфигурационный файл.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ITessaServerSettings
VB __Копировать
     Public Interface ITessaServerSettings
C++ __Копировать
     public interface class ITessaServerSettings
F# __Копировать
     type ITessaServerSettings = interface end
##  __Свойства
[CheckPlatformVersion](P_Tessa_Platform_ITessaServerSettings_CheckPlatformVersion.htm)|
Признак того, что версия платформы на клиенте и на сервере должна проверяться
на совпадение при инициализации приложения.  
---|---  
[CipherKey](P_Tessa_Platform_ITessaServerSettings_CipherKey.htm)|  Ключ,
используемый для шифрования информации в базе данных, такой как закрытые ключи
для шифрования файлов в локальных папках пользователей.  
[CipherKeyRotationInterval](P_Tessa_Platform_ITessaServerSettings_CipherKeyRotationInterval.htm)|
Интервал ротации ключей шифрования для локальных данных на компьютере
пользователя. По умолчанию равен 10 дням.  
[ConfigurationFlags](P_Tessa_Platform_ITessaServerSettings_ConfigurationFlags.htm)|
Специальные режимы конфигурации, настраиваемые в конфигурационном файле
сервера.  
[ExtensionTracingMode](P_Tessa_Platform_ITessaServerSettings_ExtensionTracingMode.htm)|
Режим трассировки расширений или null, если трассировка отключена.  
[Ldap](P_Tessa_Platform_ITessaServerSettings_Ldap.htm)| Настройки для
подключения к LDAP.  
[LicensePath](P_Tessa_Platform_ITessaServerSettings_LicensePath.htm)| Полный
путь к файлу лицензии.  
[MinConsiderableMilliseconds](P_Tessa_Platform_ITessaServerSettings_MinConsiderableMilliseconds.htm)|
Минимальное количество миллисекунд, которое должно выполняться расширение для
того, чтобы для него было создано сообщение трассировки, если используются
трассировщики [Tessa.Extensions.ExtensionTraceListenerType.ServerProfile] или
[Tessa.Extensions.ExtensionTraceListenerType.ClientProfile]. Если значение
равно 0 или отрицательное, то сообщения трассировки создаются для всех
объектов. Если значение равно null, то время выполнения расширения замеряется
с интервалом по умолчанию
[Tessa.Extensions.DefaultExtensionTraceListener.DefaultProfileMinConsiderableMilliseconds].  
[PatchList](P_Tessa_Platform_ITessaServerSettings_PatchList.htm)| Список
установленных патчей.  
[ProbingPathList](P_Tessa_Platform_ITessaServerSettings_ProbingPathList.htm)|
Список папок, используемых для загрузки сборок помимо папки с приложением.
Может содержать пути к папкам относительно папки с приложением.  
[RedisConnectionString](P_Tessa_Platform_ITessaServerSettings_RedisConnectionString.htm)|
Строка соединения с сервером или серверами Redis, или null, если Redis не
используется.  
[RoleTimeoutTimeSpan](P_Tessa_Platform_ITessaServerSettings_RoleTimeoutTimeSpan.htm)|
Таймаут выполнения длительных запросов, связанных с ролевой моделью, таких как
пересчёт замещений и пересчёт состава ролей. По умолчанию равен 30 минутам.
Таймаут рассчитывается с точностью до целых секунд с округлением в меньшую
сторону. Если указано значение 0, то запросы выполняются без таймаута, что не
рекомендуется (лучше увеличить таймаут, если по объективным обстоятельствам он
возникает).  
[ServerCode](P_Tessa_Platform_ITessaServerSettings_ServerCode.htm)| Код
сервера.  
[SessionExpirationTimeSpan](P_Tessa_Platform_ITessaServerSettings_SessionExpirationTimeSpan.htm)|
Максимальный срок жизни сессий, открываемых приложением. Срок жизни по
умолчанию - 7 дней.  
[SignatureKey](P_Tessa_Platform_ITessaServerSettings_SignatureKey.htm)| Ключ,
используемый для формирования подписи.  
[ViewAccessCacheTimeSpan](P_Tessa_Platform_ITessaServerSettings_ViewAccessCacheTimeSpan.htm)|
Максимальный интервал времени, в течение которого кэш прав доступа для каждого
сотрудника может хранится в памяти перед тем, как будет автоматически сброшен
в текущем процессе. По умолчанию равен 1 часу.  
## __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
