# NumberComposer.GetSequenceProvider - метод
Возвращает объект [Tessa.Sequences.ISequenceProvider], подходящий для
заданного события, происходящего с номером.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected virtual ISequenceProvider GetSequenceProvider(
    	INumberContext context,
    	NumberTypeDescriptor numberType
    )
VB __Копировать
     Protected Overridable Function GetSequenceProvider ( 
    	context As INumberContext,
    	numberType As NumberTypeDescriptor
    ) As ISequenceProvider
C++ __Копировать
     protected:
    virtual ISequenceProvider^ GetSequenceProvider(
    	INumberContext^ context, 
    	NumberTypeDescriptor^ numberType
    )
F# __Копировать
     abstract GetSequenceProvider : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor -> ISequenceProvider 
    override GetSequenceProvider : 
            context : INumberContext * 
            numberType : NumberTypeDescriptor -> ISequenceProvider 
#### Параметры
context [INumberContext](T_Tessa_Cards_Numbers_INumberContext.htm)
    Контекст события, происходящего с номером.
numberType
[NumberTypeDescriptor](T_Tessa_Cards_Numbers_NumberTypeDescriptor.htm)
    Тип номера, с которым выполняется действие.
#### Возвращаемое значение
[ISequenceProvider](T_Tessa_Sequences_ISequenceProvider.htm)  
Объект [Tessa.Sequences.ISequenceProvider], подходящий для заданного события,
происходящего с номером.
## __См. также
#### Ссылки
[NumberComposer - ](T_Tessa_Cards_Numbers_NumberComposer.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
