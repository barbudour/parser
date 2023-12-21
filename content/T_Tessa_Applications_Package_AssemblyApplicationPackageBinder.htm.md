# AssemblyApplicationPackageBinder - класс
Объект осуществляющий формирование пакета приложения из сборки приложения
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AssemblyApplicationPackageBinder : IApplicationPackageBinder
VB __Копировать
     Public NotInheritable Class AssemblyApplicationPackageBinder
    	Implements IApplicationPackageBinder
C++ __Копировать
     public ref class AssemblyApplicationPackageBinder sealed : IApplicationPackageBinder
F# __Копировать
     [<SealedAttribute>]
    type AssemblyApplicationPackageBinder = 
        class
            interface IApplicationPackageBinder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyApplicationPackageBinder
Implements
    [IApplicationPackageBinder](T_Tessa_Applications_Package_IApplicationPackageBinder.htm)
##  __Конструкторы
[AssemblyApplicationPackageBinder](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder__ctor.htm)|
Initializes a new instance of the AssemblyApplicationPackageBinder class.
Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Методы
[BindAsync](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_BindAsync.htm)|
Заполняет пакет приложения  
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
[OnlyForAdministrator](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_OnlyForAdministrator.htm)|
Устанавливает признак доступности приложения только администратору  
[SkipFiles](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_SkipFiles.htm)|
Задает признак необходимости обработки и помещения файлов в пакет  
[Source(Assembly)](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_Source_1.htm)|
Устанавливает в качестве источника формирования пакета приложения сборку
assembly  
[Source(Func<Assembly>)](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_Source.htm)|
Устанавливает в качестве источника функцию assemblyFunc возвращающую сборку
приложения  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WithAlias](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithAlias.htm)|
Устанавливает псевдоним приложения  
[WithApplicationKey](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithApplicationKey.htm)|
Устанавливает идентификатор приложения  
[WithApplicationName](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithApplicationName.htm)|
Устанавливает имя приложения  
[WithAppManagerApiV2](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithAppManagerApiV2.htm)|
Устанавливает, что публикуемое приложение использует новый API для
взаимодействия с менеджером приложений.  
[WithClient64Bit](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithClient64Bit.htm)|
Устанавливает, что публикуемое приложение использует 64-битную архитектуру.  
[WithGroupName](M_Tessa_Applications_Package_AssemblyApplicationPackageBinder_WithGroupName.htm)|
Устанавливает имя группы  
## __Методы расширения
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
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
