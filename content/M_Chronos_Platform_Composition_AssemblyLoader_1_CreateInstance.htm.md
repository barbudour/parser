# AssemblyLoader<TMetadata>.CreateInstance - метод
Создаёт экземпляр типа, который содержит заданную метаинформацию, используя
конструктор по умолчанию. Если тип не найден, то выбрасывается исключение.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Object CreateInstance(
    	IMetadataExportItem<TMetadata> item
    )
VB __Копировать
     Public Function CreateInstance ( 
    	item As IMetadataExportItem(Of TMetadata)
    ) As Object
C++ __Копировать
     public:
    virtual Object^ CreateInstance(
    	IMetadataExportItem<TMetadata>^ item
    ) sealed
F# __Копировать
     abstract CreateInstance : 
            item : IMetadataExportItem<'TMetadata> -> Object 
    override CreateInstance : 
            item : IMetadataExportItem<'TMetadata> -> Object 
#### Параметры
item
[IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<[TMetadata](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)>
    Экспортированная метаинформация.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Созданный экземпляр типа. Не равен null.
#### Реализации
[IAssemblyLoader<TMetadata>.CreateInstance(IMetadataExportItem<TMetadata>)](M_Chronos_Platform_Composition_IAssemblyLoader_1_CreateInstance.htm)  
##  __См. также
#### Ссылки
[AssemblyLoader<TMetadata> \-
](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
