# DiffPackageBuilderContext - класс
Контекст построения пакета содержащего информацию о файлах
## __Definition
 **Пространство имён:**
[Tessa.Applications.Package](N_Tessa_Applications_Package.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class DiffPackageBuilderContext : IApplicationPackageBuilderContext
VB __Копировать
     Public Class DiffPackageBuilderContext
    	Implements IApplicationPackageBuilderContext
C++ __Копировать
     public ref class DiffPackageBuilderContext : IApplicationPackageBuilderContext
F# __Копировать
     type DiffPackageBuilderContext = 
        class
            interface IApplicationPackageBuilderContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DiffPackageBuilderContext
Implements
    [IApplicationPackageBuilderContext](T_Tessa_Applications_Package_IApplicationPackageBuilderContext.htm)
##  __Конструкторы
[DiffPackageBuilderContext](M_Tessa_Applications_Package_DiffPackageBuilderContext__ctor.htm)|
Initializes a new instance of the DiffPackageBuilderContext class. Initializes
a new instance of the
[UpdatePackageBuilderContext](T_Tessa_Applications_Package_UpdatePackageBuilderContext.htm)
class. Инициализирует новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[BinderFactory](P_Tessa_Applications_Package_DiffPackageBuilderContext_BinderFactory.htm)|
Gets Фабрика создания объекта осуществляющего сопоставление пакета приложения
источнику  
---|---  
[ValidationResultBuilder](P_Tessa_Applications_Package_DiffPackageBuilderContext_ValidationResultBuilder.htm)|
Gets Построитель результатов валидации  
## __Методы
[BuildAsync](M_Tessa_Applications_Package_DiffPackageBuilderContext_BuildAsync.htm)|
Осуществляет построение пакета приложения  
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
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Diff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Diff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
---|---  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[MakeDiff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff_1.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackage  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[MakeDiff](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_MakeDiff.htm)|
Создает контекст построителя пакета приложения содержащий разницу между
пакетом содержащимся в построителе и пакетом updatePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[Merge](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge_1.htm)|
Создает контекст построителя пакета приложения содержащий объединение пакетов
содержащимся в построителе и пакетом mergePackage  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[Merge](M_Tessa_Applications_Package_ApplicationPackageBuilderExtender_Merge.htm)|
Создает контекст построителя пакета приложения содержащий объединение между
пакетом содержащимся в построителе и пакетом mergePackageFunc  
(Определяется
[ApplicationPackageBuilderExtender](T_Tessa_Applications_Package_ApplicationPackageBuilderExtender.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Applications.Package - пространство
имён](N_Tessa_Applications_Package.htm)
