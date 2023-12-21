# ProcessRefHelper.ParseProcessRefContainer - метод
Возвращает список ссылок на процессы, полученный из указанного XML-элемента.
## __Definition
 **Пространство имён:** [Chronos.Platform](N_Chronos_Platform.htm)  
 **Сборка:** Chronos.Platform (в Chronos.Platform.dll) Версия: 3.6.0.17
C# __Копировать
     public static IList<ProcessRef> ParseProcessRefContainer(
    	XElement refContainerElement
    )
VB __Копировать
     Public Shared Function ParseProcessRefContainer ( 
    	refContainerElement As XElement
    ) As IList(Of ProcessRef)
C++ __Копировать
     public:
    static IList<ProcessRef>^ ParseProcessRefContainer(
    	XElement^ refContainerElement
    )
F# __Копировать
     static member ParseProcessRefContainer : 
            refContainerElement : XElement -> IList<ProcessRef> 
#### Параметры
refContainerElement
[XElement](https://learn.microsoft.com/dotnet/api/system.xml.linq.xelement)
    XML-элемент, из которого будут получены ссылки на процессы.
#### Возвращаемое значение
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ProcessRef](T_Chronos_Platform_Processes_ProcessRef.htm)>  
Список ссылок на процессы, полученный из указанного XML-элемента.
##  __См. также
#### Ссылки
[ProcessRefHelper - ](T_Chronos_Platform_ProcessRefHelper.htm)
[Chronos.Platform - пространство имён](N_Chronos_Platform.htm)
