# AssemblyConsoleRegistratorFinder - класс
Выполняет поиск типов объектов
[IConsoleRegistrator](T_Tessa_Platform_ConsoleApps_IConsoleRegistrator.htm) в
заданном каталоге
[IAssemblyCatalog](T_Tessa_Platform_Composition_IAssemblyCatalog.htm).
## __Definition
 **Пространство имён:**
[Tessa.Platform.ConsoleApps](N_Tessa_Platform_ConsoleApps.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AssemblyConsoleRegistratorFinder : IFinder<ConsoleRegistratorImportingItem>
VB __Копировать
     Public NotInheritable Class AssemblyConsoleRegistratorFinder
    	Implements IFinder(Of ConsoleRegistratorImportingItem)
C++ __Копировать
     public ref class AssemblyConsoleRegistratorFinder sealed : IFinder<ConsoleRegistratorImportingItem^>
F# __Копировать
     [<SealedAttribute>]
    type AssemblyConsoleRegistratorFinder = 
        class
            interface IFinder<ConsoleRegistratorImportingItem>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyConsoleRegistratorFinder
Implements
    [IFinder](T_Tessa_Platform_Composition_IFinder_1.htm)<[ConsoleRegistratorImportingItem](T_Tessa_Platform_ConsoleApps_ConsoleRegistratorImportingItem.htm)>
##  __Конструкторы
[AssemblyConsoleRegistratorFinder](M_Tessa_Platform_ConsoleApps_AssemblyConsoleRegistratorFinder__ctor.htm)|
Создаёт экземпляр класса с указанием каталога, который используется для поиска
типов.  
---|---  
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
[Find](M_Tessa_Platform_ConsoleApps_AssemblyConsoleRegistratorFinder_Find.htm)|
Выполняет поиск объектов регистраторов для консоли и возвращает список
объектов, описывающих искомые объекты.  
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
