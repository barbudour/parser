# CardGlobalReferencesContext.MakeGlobal - метод
Сделать объект глобальным.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void MakeGlobal(
    	CardSerializableObject obj,
    	params CardSerializableObject?[] path
    )
VB __Копировать
     Public Sub MakeGlobal ( 
    	obj As CardSerializableObject,
    	ParamArray path As CardSerializableObject()
    )
C++ __Копировать
     public:
    void MakeGlobal(
    	CardSerializableObject^ obj, 
    	... array<CardSerializableObject^>^ path
    )
F# __Копировать
     member MakeGlobal : 
            obj : CardSerializableObject * 
            path : CardSerializableObject[] -> unit 
#### Параметры
obj [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)
    Целевой объект.
path [CardSerializableObject](T_Tessa_Cards_CardSerializableObject.htm)[]
    Перечень объектов, составляющих путь к данному объекту в типе карточки.
##  __См. также
#### Ссылки
[CardGlobalReferencesContext -
](T_Tessa_Cards_CardGlobalReferencesContext.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
