# ICardFileSourceOverrideSettings.FileSourceOverrides - свойство
Список объектов
[ICardFileSourceOverride](T_Tessa_Cards_ICardFileSourceOverride.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    IReadOnlyList<ICardFileSourceOverride> FileSourceOverrides { get; set; }
VB __Копировать
     Property FileSourceOverrides As IReadOnlyList(Of ICardFileSourceOverride)
    	Get
    	Set
C++ __Копировать
    property IReadOnlyList<ICardFileSourceOverride^>^ FileSourceOverrides {
    	IReadOnlyList<ICardFileSourceOverride^>^ get ();
    	void set (IReadOnlyList<ICardFileSourceOverride^>^ value);
    }
F# __Копировать
     abstract FileSourceOverrides : IReadOnlyList<ICardFileSourceOverride> with get, set
#### Значение свойства
[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<[ICardFileSourceOverride](T_Tessa_Cards_ICardFileSourceOverride.htm)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardFileSourceOverrideSettings -
](T_Tessa_Cards_ICardFileSourceOverrideSettings.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
