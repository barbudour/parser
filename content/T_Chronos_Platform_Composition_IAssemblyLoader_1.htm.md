# IAssemblyLoader<TMetadata> \- интерфейс
Объект, выполняющий загрузку метаданных и создание экземпляров типов из
сборки.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IAssemblyLoader<TMetadata>
VB __Копировать
     Public Interface IAssemblyLoader(Of TMetadata)
C++ __Копировать
    generic<typename TMetadata>
    public interface class IAssemblyLoader
F# __Копировать
     type IAssemblyLoader<'TMetadata> = interface end
#### Параметры типа
TMetadata
     Тип экспортируемых метаданных. Может реализовывать интерфейс [ISerializableMetadata<TMetadata>](T_Chronos_Contracts_ISerializableMetadata_1.htm) для сериализации. 
## __Методы
[CreateInstance](M_Chronos_Platform_Composition_IAssemblyLoader_1_CreateInstance.htm)|
Создаёт экземпляр типа, который содержит заданную метаинформацию, используя
конструктор по умолчанию. Если тип не найден, то выбрасывается исключение.  
---|---  
[Export(IReadOnlyCollection<Type>,
IAssemblyLoaderOptions)](M_Chronos_Platform_Composition_IAssemblyLoader_1_Export.htm)|
Экспортирует метаинформацию по заданному списку атрибутов.  
[Export<TAttribute>(IAssemblyLoaderOptions)](M_Chronos_Platform_Composition_IAssemblyLoader_1_Export__1.htm)|
Экспортирует метаинформацию по заданному атрибуту.  
[GetType](M_Chronos_Platform_Composition_IAssemblyLoader_1_GetType.htm)|
Возвращает тип, который содержит заданную метаинформацию. Если тип не найден,
то выбрасывается исключение.  
## __См. также
#### Ссылки
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
