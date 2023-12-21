# ConsoleRegistratorBase - класс
Базовый класс, наследуемый в объектах регистраторов консольных команд. Помимо
наследования также требуется указать атрибут
[ConsoleRegistratorAttribute](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorAttribute.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class ConsoleRegistratorBase : IConsoleRegistrator, 
    	ISealable
VB __Копировать
     Public MustInherit Class ConsoleRegistratorBase
    	Implements IConsoleRegistrator, ISealable
C++ __Копировать
     public ref class ConsoleRegistratorBase abstract : IConsoleRegistrator, 
    	ISealable
F# __Копировать
     [<AbstractClassAttribute>]
    type ConsoleRegistratorBase = 
        class
            interface IConsoleRegistrator
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ConsoleRegistratorBase
Derived
[Tessa.Extensions.Default.Console.BuildVersion.CommandRegistrator](T_Tessa_Extensions_Default_Console_BuildVersion_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.CheckCommand.CommandRegistrator](T_Tessa_Extensions_Default_Console_CheckCommand_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.CheckDatabase.CommandRegistrator](T_Tessa_Extensions_Default_Console_CheckDatabase_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.CheckService.CommandRegistrator](T_Tessa_Extensions_Default_Console_CheckService_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ConvertCards.CommandRegistrator](T_Tessa_Extensions_Default_Console_ConvertCards_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ConvertConfiguration.CommandRegistrator](T_Tessa_Extensions_Default_Console_ConvertConfiguration_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.CreateDatabase.CommandRegistrator](T_Tessa_Extensions_Default_Console_CreateDatabase_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.CreateFromTemplate.CommandRegistrator](T_Tessa_Extensions_Default_Console_CreateFromTemplate_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.DeleteCards.CommandRegistrator](T_Tessa_Extensions_Default_Console_DeleteCards_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.DropDatabase.CommandRegistrator](T_Tessa_Extensions_Default_Console_DropDatabase_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportCards.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportCards_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportLocalization.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportLocalization_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportScheme.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportScheme_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportSchemeSql.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportSchemeSql_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportSearchQueries.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportSearchQueries_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportTypes.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportTypes_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportViews.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportViews_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ExportWorkplaces.CommandRegistrator](T_Tessa_Extensions_Default_Console_ExportWorkplaces_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.FileSource.CommandRegistrator](T_Tessa_Extensions_Default_Console_FileSource_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.GetKey.CommandRegistrator](T_Tessa_Extensions_Default_Console_GetKey_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportCards.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportCards_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportLocalization.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportLocalization_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportScheme.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportScheme_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportSchemeSql.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportSchemeSql_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportSearchQueries.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportSearchQueries_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportTypes.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportTypes_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportUsers.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportUsers_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportViews.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportViews_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ImportWorkplaces.CommandRegistrator](T_Tessa_Extensions_Default_Console_ImportWorkplaces_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.IncrementVersion.CommandRegistrator](T_Tessa_Extensions_Default_Console_IncrementVersion_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.InvalidateCache.CommandRegistrator](T_Tessa_Extensions_Default_Console_InvalidateCache_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.ManageRoles.CommandRegistrator](T_Tessa_Extensions_Default_Console_ManageRoles_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.MigrateDatabase.CommandRegistrator](T_Tessa_Extensions_Default_Console_MigrateDatabase_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.MigrateFiles.CommandRegistrator](T_Tessa_Extensions_Default_Console_MigrateFiles_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.PackageApp.CommandRegistrator](T_Tessa_Extensions_Default_Console_PackageApp_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.PackageWebApp.CommandRegistrator](T_Tessa_Extensions_Default_Console_PackageWebApp_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.RebuildCalendar.CommandRegistrator](T_Tessa_Extensions_Default_Console_RebuildCalendar_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeCompact.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeCompact_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeDiff.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeDiff_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeRename.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeRename_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeScript.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeScript_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeUpdate.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeUpdate_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SchemeUpdateSql.CommandRegistrator](T_Tessa_Extensions_Default_Console_SchemeUpdateSql_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.Script.CommandRegistrator](T_Tessa_Extensions_Default_Console_Script_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SetKey.CommandRegistrator](T_Tessa_Extensions_Default_Console_SetKey_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.SqlScript.CommandRegistrator](T_Tessa_Extensions_Default_Console_SqlScript_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.TimeZone.CommandRegistrator](T_Tessa_Extensions_Default_Console_TimeZone_CommandRegistrator.htm)
[Tessa.Extensions.Default.Console.User.CommandRegistrator](T_Tessa_Extensions_Default_Console_User_CommandRegistrator.htm)
Подробнее __Less __
Implements
    [IConsoleRegistrator](T_Tessa_Platform_ConsoleApps_IConsoleRegistrator.htm), [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[ConsoleRegistratorBase](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase__ctor.htm)|
Инициализирует новый экземпляр класса ConsoleRegistratorBase  
---|---  
##  __Свойства
[CommandContext](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_CommandContext.htm)|
Контекст команд, в котором выполняется регистрация.  
---|---  
[IsSealed](P_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
##  __Методы
[CheckSealed](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RegisterCommands](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_RegisterCommands.htm)|
Выполняет регистрацию команд консоли в заданном объекте.  
[Seal](M_Tessa_Platform_ConsoleApps_ConsoleRegistratorBase_Seal.htm)| Защищает
объект от изменений.  
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
[Tessa.Platform.ConsoleApps - пространство
имён](N_Tessa_Platform_ConsoleApps.htm)
