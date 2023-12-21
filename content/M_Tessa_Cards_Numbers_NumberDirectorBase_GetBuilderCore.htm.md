# NumberDirectorBase.GetBuilderCore - метод
Возвращает объект, осуществляющий низкоуровневые действия с номерами, которые
зависят от бизнес-логики. Не возвращает null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual INumberBuilder GetBuilderCore(
    	INumberContext context
    )
VB __Копировать
     Protected Overridable Function GetBuilderCore ( 
    	context As INumberContext
    ) As INumberBuilder
C++ __Копировать
     protected:
    virtual INumberBuilder^ GetBuilderCore(
    	INumberContext^ context
    )
F# __Копировать
     abstract GetBuilderCore : 
            context : INumberContext -> INumberBuilder 
    override GetBuilderCore : 
            context : INumberContext -> INumberBuilder 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
     Контекст события, происходящего с номером, для которого возвращается объект. 
#### Возвращаемое значение
[INumberBuilder](T_Tessa_Cards_Numbers_INumberBuilder.htm)  
Объект, осуществляющий низкоуровневые действия с номерами, которые зависят от
бизнес-логики. Не возвращает null.
## __См. также
#### Ссылки
[NumberDirectorBase - ](T_Tessa_Cards_Numbers_NumberDirectorBase.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
