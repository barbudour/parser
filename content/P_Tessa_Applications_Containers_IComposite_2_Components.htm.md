# IComposite<TComponent, TOperation>.Components - свойство
Gets Возвращает список компонентов контейнера расположенных непосредственно в
самом контейнере.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Containers](N_Tessa_Applications_Containers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [NotNullAttribute]
    IEnumerable<TComponent> Components { get; }
VB __Копировать
    <NotNullAttribute>
    ReadOnly Property Components As IEnumerable(Of TComponent)
    	Get
C++ __Копировать
    [NotNullAttribute]
    property IEnumerable<TComponent>^ Components {
    	IEnumerable<TComponent>^ get ();
    }
F# __Копировать
     [<NotNullAttribute>]
    abstract Components : IEnumerable<'TComponent> with get
#### Значение свойства
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[TComponent](T_Tessa_Applications_Containers_IComposite_2.htm)>
##  __См. также
#### Ссылки
[IComposite<TComponent, TOperation> \-
](T_Tessa_Applications_Containers_IComposite_2.htm)
[Tessa.Applications.Containers - пространство
имён](N_Tessa_Applications_Containers.htm)
