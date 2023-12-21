# AssemblyLoader<TMetadata> \- класс
Объект, выполняющий загрузку метаданных и создание экземпляров типов из
сборки.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class AssemblyLoader<TMetadata> : IAssemblyLoader<TMetadata>
VB __Копировать
     Public NotInheritable Class AssemblyLoader(Of TMetadata)
    	Implements IAssemblyLoader(Of TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public ref class AssemblyLoader sealed : IAssemblyLoader<TMetadata>
F# __Копировать
     [<SealedAttribute>]
    type AssemblyLoader<'TMetadata> = 
        class
            interface IAssemblyLoader<'TMetadata>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AssemblyLoader<TMetadata>
Implements
    [IAssemblyLoader](T_Chronos_Platform_Composition_IAssemblyLoader_1.htm)<TMetadata>
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm) для сериализации. 
## __Конструкторы
[AssemblyLoader<TMetadata>](M_Chronos_Platform_Composition_AssemblyLoader_1__ctor.htm)|
Создаёт экземпляр класса с указанием каталога, из которого выполняется экспорт
метаинформации.  
---|---  
## __Методы
[CreateInstance](M_Chronos_Platform_Composition_AssemblyLoader_1_CreateInstance.htm)|
Создаёт экземпляр типа, который содержит заданную метаинформацию, используя
конструктор по умолчанию. Если тип не найден, то выбрасывается исключение.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Export(IReadOnlyCollection<Type>,
IAssemblyLoaderOptions)](M_Chronos_Platform_Composition_AssemblyLoader_1_Export.htm)|
Экспортирует метаинформацию по заданному списку атрибутов.  
[Export<TAttribute>(IAssemblyLoaderOptions)](M_Chronos_Platform_Composition_AssemblyLoader_1_Export__1.htm)|
Экспортирует метаинформацию по заданному атрибуту.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType(IMetadataExportItem<TMetadata>)](M_Chronos_Platform_Composition_AssemblyLoader_1_GetType.htm)|
Возвращает тип, который содержит заданную метаинформацию. Если тип не найден,
то выбрасывается исключение.  
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
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
