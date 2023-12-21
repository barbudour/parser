# CommandRegistrator - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Console.ExportSchemeSql](N_Tessa_Extensions_Default_Console_ExportSchemeSql.htm)  
 **Сборка:** Tessa.Extensions.Default.Console (в
Tessa.Extensions.Default.Console.dll) Версия: 3.6.0.17
C# __Копировать
    [ConsoleRegistratorAttribute(ExtensionStage.AfterPlatform)]
    public sealed class CommandRegistrator : ConsoleRegistratorBase
VB __Копировать
    <ConsoleRegistratorAttribute(ExtensionStage.AfterPlatform)>
    Public NotInheritable Class CommandRegistrator
    	Inherits ConsoleRegistratorBase
C++ __Копировать
    [ConsoleRegistratorAttribute(ExtensionStage::AfterPlatform)]
    public ref class CommandRegistrator sealed : public ConsoleRegistratorBase
F# __Копировать
     [<SealedAttribute>]
    [<ConsoleRegistratorAttribute(ExtensionStage.AfterPlatform)>]
    type CommandRegistrator = 
        class
            inherit ConsoleRegistratorBase
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm) __ CommandRegistrator
##  __Конструкторы
[CommandRegistrator](M_Tessa_Extensions_Default_Console_ExportSchemeSql_CommandRegistrator__ctor.htm)|
Инициализирует новый экземпляр класса CommandRegistrator  
---|---  
##  __Свойства
[CommandContext](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_CommandContext.htm)|
Контекст команд, в котором выполняется регистрация.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
---|---  
[IsSealed](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
##  __Методы
[CheckSealed](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FinalizeRegistration](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_FinalizeRegistration.htm)|
Завершает регистрацию после того, как все команды инициализированы.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
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
[InitializeRegistration](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_InitializeRegistration.htm)|
Инициализирует регистрацию перед тем, как какие-либо команды были добавлены.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterCommands](M_Tessa_Extensions_Default_Console_ExportSchemeSql_CommandRegistrator_RegisterCommands.htm)|  
(Переопределяет
[ConsoleRegistratorBase.RegisterCommands()](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_RegisterCommands.htm))  
[Seal](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_Seal.htm)| Защищает
объект от изменений.  
(Унаследован от
[ConsoleRegistratorBase](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase.htm))  
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
[Tessa.Extensions.Default.Console.ExportSchemeSql - пространство
имён](N_Tessa_Extensions_Default_Console_ExportSchemeSql.htm)
