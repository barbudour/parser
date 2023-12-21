# TessaServerSettings - класс
Настройки TESSA на сервере, которые выносятся в конфигурационный файл.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TessaServerSettings : ITessaServerSettings
VB __Копировать
     Public NotInheritable Class TessaServerSettings
    	Implements ITessaServerSettings
C++ __Копировать
     public ref class TessaServerSettings sealed : ITessaServerSettings
F# __Копировать
     [<SealedAttribute>]
    type TessaServerSettings = 
        class
            interface ITessaServerSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaServerSettings
Implements
    [ITessaServerSettings](T_Tessa_Platform_ITessaServerSettings.htm)
##  __Конструкторы
[TessaServerSettings](M_Tessa_Platform_TessaServerSettings__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[CheckPlatformVersion](P_Tessa_Platform_TessaServerSettings_CheckPlatformVersion.htm)|
Признак того, что версия платформы на клиенте и на сервере должна проверяться
на совпадение при инициализации приложения.  
---|---  
[CipherKey](P_Tessa_Platform_TessaServerSettings_CipherKey.htm)|  Ключ,
используемый для шифрования информации в базе данных, такой как закрытые ключи
для шифрования файлов в локальных папках пользователей.  
[CipherKeyRotationInterval](P_Tessa_Platform_TessaServerSettings_CipherKeyRotationInterval.htm)|
Интервал ротации ключей шифрования для локальных данных на компьютере
пользователя. По умолчанию равен 10 дням.  
[ConfigurationFlags](P_Tessa_Platform_TessaServerSettings_ConfigurationFlags.htm)|
Специальные режимы конфигурации, настраиваемые в конфигурационном файле
сервера.  
[ExtensionTracingMode](P_Tessa_Platform_TessaServerSettings_ExtensionTracingMode.htm)|
Режим трассировки расширений или null, если трассировка отключена.  
[Ldap](P_Tessa_Platform_TessaServerSettings_Ldap.htm)| Настройки для
подключения к LDAP.  
[LicensePath](P_Tessa_Platform_TessaServerSettings_LicensePath.htm)| Полный
путь к файлу лицензии.  
[MinConsiderableMilliseconds](P_Tessa_Platform_TessaServerSettings_MinConsiderableMilliseconds.htm)|
Минимальное количество миллисекунд, которое должно выполняться расширение для
того, чтобы для него было создано сообщение трассировки, если используются
трассировщики [Tessa.Extensions.ExtensionTraceListenerType.ServerProfile] или
[Tessa.Extensions.ExtensionTraceListenerType.ClientProfile]. Если значение
равно 0 или отрицательное, то сообщения трассировки создаются для всех
объектов. Если значение равно null, то время выполнения расширения замеряется
с интервалом по умолчанию
[Tessa.Extensions.DefaultExtensionTraceListener.DefaultProfileMinConsiderableMilliseconds].  
[PatchList](P_Tessa_Platform_TessaServerSettings_PatchList.htm)| Список
установленных патчей.  
[ProbingPathList](P_Tessa_Platform_TessaServerSettings_ProbingPathList.htm)|
Список папок, используемых для загрузки сборок помимо папки с приложением.
Может содержать пути к папкам относительно папки с приложением.  
[RedisConnectionString](P_Tessa_Platform_TessaServerSettings_RedisConnectionString.htm)|
Строка соединения с сервером или серверами Redis, или null, если Redis не
используется.  
[RoleTimeoutTimeSpan](P_Tessa_Platform_TessaServerSettings_RoleTimeoutTimeSpan.htm)|
Таймаут выполнения длительных запросов, связанных с ролевой моделью, таких как
пересчёт замещений и пересчёт состава ролей. По умолчанию равен 30 минутам.
Таймаут рассчитывается с точностью до целых секунд с округлением в меньшую
сторону. Если указано значение 0, то запросы выполняются без таймаута, что не
рекомендуется (лучше увеличить таймаут, если по объективным обстоятельствам он
возникает).  
[ServerCode](P_Tessa_Platform_TessaServerSettings_ServerCode.htm)| Код
сервера.  
[SessionExpirationTimeSpan](P_Tessa_Platform_TessaServerSettings_SessionExpirationTimeSpan.htm)|
Максимальный срок жизни сессий, открываемых приложением. Срок жизни по
умолчанию - 7 дней.  
[SignatureKey](P_Tessa_Platform_TessaServerSettings_SignatureKey.htm)| Ключ,
используемый для формирования подписи.  
[ViewAccessCacheTimeSpan](P_Tessa_Platform_TessaServerSettings_ViewAccessCacheTimeSpan.htm)|
Максимальный интервал времени, в течение которого кэш прав доступа для каждого
сотрудника может хранится в памяти перед тем, как будет автоматически сброшен
в текущем процессе. По умолчанию равен 1 часу.  
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
[SetFromConfig](M_Tessa_Platform_TessaServerSettings_SetFromConfig.htm)|
Устанавливает значения настроек из файла конфигурации.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
