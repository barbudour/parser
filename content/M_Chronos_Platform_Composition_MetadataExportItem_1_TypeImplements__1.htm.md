# MetadataExportItem<TMetadata>.TypeImplements<T> \- метод
Возвращает признак того, что экспортированный тип реализует указанный
интерфейс.
##  __Definition
 **Пространство имён:**
[Chronos.Platform.Composition](N_Chronos_Platform_Composition.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public bool TypeImplements<T>()
VB __Копировать
     Public Function TypeImplements(Of T) As Boolean
C++ __Копировать
     public:
    generic<typename T>
    virtual bool TypeImplements() sealed
F# __Копировать
     abstract TypeImplements : unit -> bool 
    override TypeImplements : unit -> bool 
#### Параметры типа
T
    Тип интерфейса, для которого будет выполняться проверка.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если экспортированный тип реализует указанный интерфейс; false в
противном случае.
#### Реализации
[IMetadataExportItem<TMetadata>.TypeImplements<T>()](M_Chronos_Platform_Composition_IMetadataExportItem_1_TypeImplements__1.htm)  
##  __См. также
#### Ссылки
[MetadataExportItem<TMetadata> \-
](T_Chronos_Platform_Composition_MetadataExportItem_1.htm)
[Chronos.Platform.Composition - пространство
имён](N_Chronos_Platform_Composition.htm)
