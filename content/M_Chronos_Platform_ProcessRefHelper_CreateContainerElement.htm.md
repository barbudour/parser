# ProcessRefHelper.CreateContainerElement - метод
Создаёт XML-элемент, описывающий указанное перечисление ссылок на процессы.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static XElement CreateContainerElement(
    	IEnumerable<ProcessRef> processRefItems
    )
VB __Копировать
     Public Shared Function CreateContainerElement ( 
    	processRefItems As IEnumerable(Of ProcessRef)
    ) As XElement
C++ __Копировать
     public:
    static XElement^ CreateContainerElement(
    	IEnumerable<ProcessRef>^ processRefItems
    )
F# __Копировать
     static member CreateContainerElement : 
            processRefItems : IEnumerable<ProcessRef> -> XElement 
#### Параметры
processRefItems
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>
    Перечисление ссылок на процессы, которые будут сохранены в XML-элементе.
#### Возвращаемое значение
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)  
XML-элемент, описывающий указанное перечисление ссылок на процессы.
##  __См. также
#### Ссылки
[ProcessRefHelper - ](T_Chronos_Platform_ProcessRefHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
