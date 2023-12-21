# CardSchemeInfoProviderAdapter(ICardSchemeInfoProvider, ISchemeService) -
конструктор
Создаёт экземпляр класса с указанием объекта, для которого выполняется
адаптация к интерфейсу [ISchemeService](T_Tessa_Scheme_ISchemeService.htm), и
указанием объекта [ISchemeService](T_Tessa_Scheme_ISchemeService.htm) для
получения других объектов, кроме таблиц.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardSchemeInfoProviderAdapter(
    	ICardSchemeInfoProvider schemeInfoProvider,
    	ISchemeService schemeService
    )
VB __Копировать
     Public Sub New ( 
    	schemeInfoProvider As ICardSchemeInfoProvider,
    	schemeService As ISchemeService
    )
C++ __Копировать
     public:
    CardSchemeInfoProviderAdapter(
    	ICardSchemeInfoProvider^ schemeInfoProvider, 
    	ISchemeService^ schemeService
    )
F# __Копировать
     new : 
            schemeInfoProvider : ICardSchemeInfoProvider * 
            schemeService : ISchemeService -> CardSchemeInfoProviderAdapter
#### Параметры
schemeInfoProvider
[ICardSchemeInfoProvider](T_Tessa_Cards_ICardSchemeInfoProvider.htm)
    Адаптируемый объект.
schemeService [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
     Сервис схемы данных, используемый для получения всех объектов, кроме таблиц. Значения проксируются при вызове методов. Не должен быть равен null. 
## __См. также
#### Ссылки
[CardSchemeInfoProviderAdapter -
](T_Tessa_Cards_CardSchemeInfoProviderAdapter.htm)
[CardSchemeInfoProviderAdapter -
перегрузка](Overload_Tessa_Cards_CardSchemeInfoProviderAdapter__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
