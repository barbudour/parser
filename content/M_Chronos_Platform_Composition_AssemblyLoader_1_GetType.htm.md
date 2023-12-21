# AssemblyLoader<TMetadata>.GetType(IMetadataExportItem<TMetadata>) - метод
Возвращает тип, который содержит заданную метаинформацию. Если тип не найден,
то выбрасывается исключение.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public Type GetType(
    	IMetadataExportItem<TMetadata> item
    )
VB __Копировать
     Public Function GetType ( 
    	item As IMetadataExportItem(Of TMetadata)
    ) As Type
C++ __Копировать
     public:
    virtual Type^ GetType(
    	IMetadataExportItem<TMetadata>^ item
    ) sealed
F# __Копировать
     abstract GetType : 
            item : IMetadataExportItem<'TMetadata> -> Type 
    override GetType : 
            item : IMetadataExportItem<'TMetadata> -> Type 
#### Параметры
item
[IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<[TMetadata](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)>
    Экспортированная метаинформация.
#### Возвращаемое значение
[Type](https://learn.microsoft.com/dotnet/api/system.type)  
Тип, который содержит заданную метаинформацию. Не равен null.
#### Реализации
[IAssemblyLoader<TMetadata>.GetType(IMetadataExportItem<TMetadata>)](M_Chronos_Platform_Composition_IAssemblyLoader_1_GetType.htm)  
##  __См. также
#### Ссылки
[AssemblyLoader<TMetadata> \-
](T_Chronos_Platform_Composition_AssemblyLoader_1.htm)
[GetType -
перегрузка](Overload_Chronos_Platform_Composition_AssemblyLoader_1_GetType.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
