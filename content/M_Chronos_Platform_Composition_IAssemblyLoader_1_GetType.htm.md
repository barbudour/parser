# IAssemblyLoader<TMetadata>.GetType - метод
Возвращает тип, который содержит заданную метаинформацию. Если тип не найден,
то выбрасывается исключение.
## __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     Type GetType(
    	IMetadataExportItem<TMetadata> item
    )
VB __Копировать
     Function GetType ( 
    	item As IMetadataExportItem(Of TMetadata)
    ) As Type
C++ __Копировать
    Type^ GetType(
    	IMetadataExportItem<TMetadata>^ item
    )
F# __Копировать
     abstract GetType : 
            item : IMetadataExportItem<'TMetadata> -> Type 
#### Параметры
item
[IMetadataExportItem](T_Chronos_Platform_Composition_IMetadataExportItem_1.htm)<[TMetadata](T_Chronos_Platform_Composition_IAssemblyLoader_1.htm)>
    Экспортированная метаинформация.
#### Возвращаемое значение
[Type](https://learn.microsoft.com/dotnet/api/system.type)  
Тип, который содержит заданную метаинформацию. Не равен null.
## __См. также
#### Ссылки
[IAssemblyLoader<TMetadata> \-
](T_Chronos_Platform_Composition_IAssemblyLoader_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
