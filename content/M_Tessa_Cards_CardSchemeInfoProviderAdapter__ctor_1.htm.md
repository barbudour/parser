# CardSchemeInfoProviderAdapter(ICardSchemeInfoProvider, SchemeDatabase) -
конструктор
Создаёт экземпляр класса с указанием объекта, для которого выполняется
адаптация к интерфейсу [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), и
опциональным указанием объекта
[SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm) для получения других
объектов, кроме таблиц.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSchemeInfoProviderAdapter(
    	ICardSchemeInfoProvider schemeInfoProvider,
    	SchemeDatabase schemeDatabase = null
    )
VB __Копировать
     Public Sub New ( 
    	schemeInfoProvider As ICardSchemeInfoProvider,
    	Optional schemeDatabase As SchemeDatabase = Nothing
    )
C++ __Копировать
     public:
    CardSchemeInfoProviderAdapter(
    	ICardSchemeInfoProvider^ schemeInfoProvider, 
    	SchemeDatabase^ schemeDatabase = nullptr
    )
F# __Копировать
     new : 
            schemeInfoProvider : ICardSchemeInfoProvider * 
            ?schemeDatabase : SchemeDatabase 
    (* Defaults:
            let _schemeDatabase = defaultArg schemeDatabase null
    *)
    -> CardSchemeInfoProviderAdapter
#### Параметры
schemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
    Адаптируемый объект.
schemeDatabase [SchemeDatabase](T_Tessa_Scheme_SchemeDatabase.htm) (Optional)
     Схема базы данных, используемая для получения всех объектов, кроме таблиц. Значения сохраняются на момент вызова конструктора. Если указано null, то объект не возвращает других объектов, кроме таблиц. 
## __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[CardSchemeInfoProviderAdapter -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
