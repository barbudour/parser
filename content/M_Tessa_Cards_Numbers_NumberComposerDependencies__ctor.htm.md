# NumberComposerDependencies - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:** [Tessa.Cards.Numbers](N_Tessa_Cards_Numbers.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public NumberComposerDependencies(
    	ISequenceProvider sequenceProviderDefault,
    	ISequenceProvider sequenceProviderWithoutTransaction
    )
VB __Копировать
     Public Sub New ( 
    	sequenceProviderDefault As ISequenceProvider,
    	sequenceProviderWithoutTransaction As ISequenceProvider
    )
C++ __Копировать
     public:
    NumberComposerDependencies(
    	ISequenceProvider^ sequenceProviderDefault, 
    	ISequenceProvider^ sequenceProviderWithoutTransaction
    )
F# __Копировать
     new : 
            sequenceProviderDefault : ISequenceProvider * 
            sequenceProviderWithoutTransaction : ISequenceProvider -> NumberComposerDependencies
#### Параметры
sequenceProviderDefault
[ISequenceProvider](T_Tessa_Sequences_ISequenceProvider.htm)
     Реализация сервиса [ISequenceProvider](T_Tessa_Sequences_ISequenceProvider.htm), выполняющая все запросы в транзакции. Не может быть равна null. 
sequenceProviderWithoutTransaction
[ISequenceProvider](T_Tessa_Sequences_ISequenceProvider.htm)
     Реализация сервиса [ISequenceProvider](T_Tessa_Sequences_ISequenceProvider.htm), выполняющая все запросы без транзакции. Не может быть равна null. 
## __См. также
#### Ссылки
[NumberComposerDependencies -
](T_Tessa_Cards_Numbers_NumberComposerDependencies.htm)
[Tessa.Cards.Numbers - пространство имён](N_Tessa_Cards_Numbers.htm)
