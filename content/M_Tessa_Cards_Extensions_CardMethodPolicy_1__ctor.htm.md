# CardMethodPolicy<TMethod> \- конструктор
Создаёт экземпляр класса с указанием списка допустимых методов выполнения
запроса к API карточек.
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMethodPolicy(
    	params TMethod[] methods
    )
VB __Копировать
     Public Sub New ( 
    	ParamArray methods As TMethod()
    )
C++ __Копировать
     public:
    CardMethodPolicy(
    	... array<TMethod>^ methods
    )
F# __Копировать
     new : 
            methods : 'TMethod[] -> CardMethodPolicy
#### Параметры
methods [TMethod](T_Tessa_Cards_Extensions_CardMethodPolicy_1.htm)[]
    Список допустимых методов выполнения запроса к API карточек.
##  __См. также
#### Ссылки
[CardMethodPolicy<TMethod> \-
](T_Tessa_Cards_Extensions_CardMethodPolicy_1.htm)
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
