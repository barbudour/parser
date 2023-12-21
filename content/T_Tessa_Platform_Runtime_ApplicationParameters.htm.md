# ApplicationParameters - класс
Параметры запуска приложения
[IApplication](T_Tessa_Platform_Runtime_IApplication.htm), которые были
определены в ходе запуска.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ApplicationParameters : IApplicationParameters
VB __Копировать
     Public NotInheritable Class ApplicationParameters
    	Implements IApplicationParameters
C++ __Копировать
     public ref class ApplicationParameters sealed : IApplicationParameters
F# __Копировать
     [<SealedAttribute>]
    type ApplicationParameters = 
        class
            interface IApplicationParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ApplicationParameters
Implements
    [IApplicationParameters](T_Tessa_Platform_Runtime_IApplicationParameters.htm)
##  __Конструкторы
[ApplicationParameters](M_Tessa_Platform_Runtime_ApplicationParameters__ctor.htm)|
Инициализирует новый экземпляр класса ApplicationParameters  
---|---  
##  __Свойства
[AppManagerApi](P_Tessa_Platform_Runtime_ApplicationParameters_AppManagerApi.htm)|
Номер версии API для взаимодействия текущего приложения с TessaAppManager,
который выполнил запуск этого приложения. 0, если приложение не запущено из
TessaAppManager, 1, если приложение использует первую версию API, 2 \- если
вторую версию API, и т.д.  
---|---  
[AppManagerVersion](P_Tessa_Platform_Runtime_ApplicationParameters_AppManagerVersion.htm)|
Полная строка имени сборки для приложения TessaAppManager, которое запустило
текущее приложение, или null, если приложение не запущено из TessaAppManager.
Используйте вспомогательный метод
[Tessa.Platform.Runtime.RuntimeHelper.ParseBuildVersionString] для того, чтобы
получить отдельные компоненты из строки версии.  
[AutoStart](P_Tessa_Platform_Runtime_ApplicationParameters_AutoStart.htm)|
Признак того, что приложение запущено с параметром "при автозапуске Windows".
Если приложение поддерживает этот параметр, то экран загрузки и окно
приложения не отображаются, приложение свёрнуто в трей. Среди стандартных
приложений платформы поддержкой этого параметра обладает только приложение
TessaAppManager.  
[BaseAddress](P_Tessa_Platform_Runtime_ApplicationParameters_BaseAddress.htm)|
Базовый адрес для подключения приложения.  
[Info](P_Tessa_Platform_Runtime_ApplicationParameters_Info.htm)|
Дополнительная информация, связанная с параметрами запуска.  
[InstanceName](P_Tessa_Platform_Runtime_ApplicationParameters_InstanceName.htm)|
Имя экземпляра сервера, к которому подключается приложение.  
[LaunchedByAppManager](P_Tessa_Platform_Runtime_ApplicationParameters_LaunchedByAppManager.htm)|
Приложение было запущено из Tessa Applications. Обычно параметр
устанавливается в переменных окружения.  
[Links](P_Tessa_Platform_Runtime_ApplicationParameters_Links.htm)| Коллекция
ссылок, которые должны быть обработаны после запуска приложения.  
[Login](P_Tessa_Platform_Runtime_ApplicationParameters_Login.htm)| Логин
пользователя, выполняющего вход в приложение. Также должен быть задан пароль.  
[MetadataCacheFilePath](P_Tessa_Platform_Runtime_ApplicationParameters_MetadataCacheFilePath.htm)|
Путь к файлу с кэшом метаинформации, который должен использоваться вместо
стандартного файла, или null/пустая строка, если используется стандартный
файл.  
[NotificationsAreEnabled](P_Tessa_Platform_Runtime_ApplicationParameters_NotificationsAreEnabled.htm)|
Признак того, что приложению разрешается выводить всплывающие уведомления в
правом нижнем углу экрана, обычно - уведомления по заданиям. Передаётся от
диспетчера приложений. Если приложение запущено пользователем вручную (не
через диспетчер) или если через диспетчер открывается первый экземпляр
приложения на этом сервере, то указывается значение true и приложению
разрешается выводить уведомления. Если запускается ещё один экземпляр
приложения на том же сервере, то ему передаётся значение false.  
[Password](P_Tessa_Platform_Runtime_ApplicationParameters_Password.htm)|
Пароль пользователя, выполняющего вход в приложение. Также должен быть задан
логин.  
[PublishApplicationName](P_Tessa_Platform_Runtime_ApplicationParameters_PublishApplicationName.htm)|
Имя приложения, с которым оно будет опубликовано, или null, если используется
имя приложения по умолчанию при первой публикации или имя приложения не
изменяется при повторной публикации. Параметр имеет смысл только тогда, когда
признак [Tessa.Platform.Runtime.IApplicationParameters.PublishMode] указан как
true.  
[PublishAppManagerApiV2](P_Tessa_Platform_Runtime_ApplicationParameters_PublishAppManagerApiV2.htm)|
Указывает, что публикуемое приложение использует новый API для взаимодействия
с менеджером приложений. Рекомендуется указать true для desktop-приложений
TESSA, начиная со сборки 3.5.0. Требуется использовать совместно с командой
Publish. По умолчанию равно true, поскольку приложения в текущей сборке
поддерживают новое API.  
[PublishClient64Bit](P_Tessa_Platform_Runtime_ApplicationParameters_PublishClient64Bit.htm)|
Указывает, что публикуемое приложение использует 64-битную архитектуру. Если
равно true, то приложение нельзя запустить на 32-битных ОС. Требуется
использовать совместно с командой Publish. По умолчанию равно true, если
текущий выполняем процесс является 64-битным, и false в противном случае.  
[PublishForAdmin](P_Tessa_Platform_Runtime_ApplicationParameters_PublishForAdmin.htm)|
Признак того, что приложение публикуется только для администраторов. Параметр
имеет смысл только тогда, когда признак
[Tessa.Platform.Runtime.IApplicationParameters.PublishMode] указан как true.  
[PublishGroupName](P_Tessa_Platform_Runtime_ApplicationParameters_PublishGroupName.htm)|
Имя группы, в которую приложение будет опубликовано, или null, если
используется пустая группа при первой публикации или группа приложения не
изменяется при повторной публикации. Если явно указана пустая строка, то
приложение публикуется без группы даже при повторной публикации. Параметр
имеет смысл только тогда, когда признак
[Tessa.Platform.Runtime.IApplicationParameters.PublishMode] указан как true.  
[PublishInstanceName](P_Tessa_Platform_Runtime_ApplicationParameters_PublishInstanceName.htm)|
Имя экземпляра сервера, в который будет опубликовано приложение, или null,
если публикация выполняется для того же экземпляра, в который выполняется
логин. Параметр имеет смысл только тогда, когда признак
[Tessa.Platform.Runtime.IApplicationParameters.PublishMode] указан как true.  
[PublishMode](P_Tessa_Platform_Runtime_ApplicationParameters_PublishMode.htm)|
Режим публикации приложения, когда вместо запуска приложение публикует себя на
сервере.  
[PublishQuiet](P_Tessa_Platform_Runtime_ApplicationParameters_PublishQuiet.htm)|
Признак того, что приложение публикуется без использования UI, т.е. с выводом
только в лог. Параметр имеет смысл только тогда, когда признак
[Tessa.Platform.Runtime.IApplicationParameters.PublishMode] указан как true.  
[SkipWinAuth](P_Tessa_Platform_Runtime_ApplicationParameters_SkipWinAuth.htm)|
Признак того, что при незаданных параметрах логина/пароля пропускается попытка
Windows-аутентификации.  
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
[Set](M_Tessa_Platform_Runtime_ApplicationParameters_Set.htm)| Устанавливает
свойства текущего объекта по свойствам заданного объекта.  
[SetConnectionSettings](M_Tessa_Platform_Runtime_ApplicationParameters_SetConnectionSettings.htm)|
Устанавливает свойства текущего объекта по заданным параметрам подключения.  
[SetCredentials](M_Tessa_Platform_Runtime_ApplicationParameters_SetCredentials.htm)|
Устанавливает свойства текущего объекта по заданным параметрам входа.  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
