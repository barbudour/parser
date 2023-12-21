# ICardSerializableObjectContext.GlobalReferences - свойство
Словарь, содержащий глобальные объекты
([CardTypeForm](T_Tessa_Cards_CardTypeForm.htm),
[CardTypeBlock](T_Tessa_Cards_CardTypeBlock.htm),
[CardTypeControl](T_Tessa_Cards_CardTypeControl.htm),
[CardTypeValidator](T_Tessa_Cards_CardTypeValidator.htm),
[CardTypeExtension](T_Tessa_Cards_CardTypeExtension.htm)), совместно
использующиеся в типах карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    HashSet<string, CardSerializableObject> GlobalReferences { get; }
VB __Копировать
     ReadOnly Property GlobalReferences As HashSet(Of String, CardSerializableObject)
    	Get
C++ __Копировать
    property HashSet<String^, CardSerializableObject^>^ GlobalReferences {
    	HashSet<String^, CardSerializableObject^>^ get ();
    }
F# __Копировать
     abstract GlobalReferences : HashSet<string, CardSerializableObject> with get
#### Значение свойства
[HashSet](T_Tessa_Platform_Collections_HashSet_2.htm)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)>
##  __См. также
#### Ссылки
[ICardSerializableObjectContext -
](T_Tessa_Cards_ICardSerializableObjectContext.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
