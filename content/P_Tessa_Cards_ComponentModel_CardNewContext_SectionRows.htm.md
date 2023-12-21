# CardNewContext.SectionRows - свойство
Пустые строки коллекционных или древовидных секций создаваемой карточки,
доступные по имени секции. Требуется инициализация посредством метода
[InitResponse(CardNewResponse)](M_Tessa_Cards_ComponentModel_CardNewContext_InitResponse.htm),
в противном случае возвращает null.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public StringDictionaryStorage<CardRow> SectionRows { get; }
VB __Копировать
     Public ReadOnly Property SectionRows As StringDictionaryStorage(Of CardRow)
    	Get
C++ __Копировать
     public:
    property StringDictionaryStorage<CardRow^>^ SectionRows {
    	StringDictionaryStorage<CardRow^>^ get ();
    }
F# __Копировать
     member SectionRows : StringDictionaryStorage<CardRow> with get
#### Значение свойства
[StringDictionaryStorage](T_Tessa_Platform_Storage_StringDictionaryStorage_1.htm)<[CardRow](T_Tessa_Cards_CardRow.htm)>
##  __См. также
#### Ссылки
[CardNewContext - ](T_Tessa_Cards_ComponentModel_CardNewContext.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
