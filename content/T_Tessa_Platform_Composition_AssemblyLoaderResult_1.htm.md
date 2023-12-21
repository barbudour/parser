# AssemblyLoaderResult<TMetadata> \- класс
Результат загрузки метаданных из сборок.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Composition](N_Tessa_Platform_Composition.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AssemblyLoaderResult<TMetadata> : IAssemblyLoaderResult<TMetadata>
VB __Копировать
     Public Class AssemblyLoaderResult(Of TMetadata)
    	Implements IAssemblyLoaderResult(Of TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public ref class AssemblyLoaderResult : IAssemblyLoaderResult<TMetadata>
F# __Копировать
     type AssemblyLoaderResult<'TMetadata> = 
        class
            interface IAssemblyLoaderResult<'TMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyLoaderResult<TMetadata>
Implements
    [IAssemblyLoaderResult](T_Tessa_Platform_Composition_IAssemblyLoaderResult_1.htm)<TMetadata>
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Tessa_Platform_Composition_ISerializableMetadata_1.htm) для сериализации. 
## __Заметки
Наследники класса могут добавлять свойства.
## __Конструкторы
[AssemblyLoaderResult<TMetadata>](M_Tessa_Platform_Composition_AssemblyLoaderResult_1__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойств.  
---|---  
## __Свойства
[AssemblyResolvers](P_Tessa_Platform_Composition_AssemblyLoaderResult_1_AssemblyResolvers.htm)|
Объекты, выполнявшие загрузку сборок в процессе экспорта метаинформации.  
---|---  
[Items](P_Tessa_Platform_Composition_AssemblyLoaderResult_1_Items.htm)| Вся
экспортированная метаинформация.  
[Options](P_Tessa_Platform_Composition_AssemblyLoaderResult_1_Options.htm)|
Настройки, использованные при экспорте метаинформации.  
##  __Методы
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
[Tessa.Platform.Composition - пространство
имён](N_Tessa_Platform_Composition.htm)
