# NumberComposer.TryCreateNewDbScope - метод
Открывает новое соединение с базой данных, если этого требует режим выполнения
транзакций и выполнение происходит на сервере. В противном случае возвращает
null.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual IDbScopeInstance TryCreateNewDbScope(
    	INumberContext context,
    	NumberTypeDescriptor numberType
    )
VB __Копировать
     Protected Overridable Function TryCreateNewDbScope ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor
    ) As IDbScopeInstance
C++ __Копировать
     protected:
    virtual IDbScopeInstance^ TryCreateNewDbScope(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType
    )
F# __Копировать
     abstract TryCreateNewDbScope : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor -> IDbScopeInstance 
    override TryCreateNewDbScope : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor -> IDbScopeInstance 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера, с которым выполняется действие.
#### Возвращаемое значение
[IDbScopeInstance](T_Tessa_Platform_Data_IDbScopeInstance.htm)  
Новое соединение с базой данных, если этого требует режим выполнения
транзакций и выполнение происходит на сервере, или null в противном случае.
## __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
