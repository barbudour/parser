# NumberDirectorBase.UnavailableCardTypes - свойство
Идентификаторы типов карточек, система нумерации для которых принудительно
отключена.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual HashSet<Guid> UnavailableCardTypes { get; }
VB __Копировать
     Protected Overridable ReadOnly Property UnavailableCardTypes As HashSet(Of Guid)
    	Get
C++ __Копировать
     protected:
    virtual property HashSet<Guid>^ UnavailableCardTypes {
    	HashSet<Guid>^ get ();
    }
F# __Копировать
     abstract UnavailableCardTypes : HashSet<Guid> with get
    override UnavailableCardTypes : HashSet<Guid> with get
#### Значение свойства
[HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
