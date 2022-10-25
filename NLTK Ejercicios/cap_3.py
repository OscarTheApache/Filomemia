Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
>>> len(vocabulario)
4017
>>> vocabulario[100:130]
['41', '42', '43', '44', '45', '46', '47', '48', '49', '5', '5.', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '6', '60', '61', '62', '63', '64', '65', '66', '67']
>>> vocabulario[50:80]
['136', '137', '138', '139', '14', '140', '141', '142', '143', '144', '145', '146', '147', '14th', '15', '16', '17', '18', '183', '19', '2', '20', '200,000', '2008', '21', '22', '23', '24', '241', '241â€™s']
>>> vocabulario[1:15]
["'d", '(', ')', ',', '-', '.', '...', '/ext', '1', '10', '100', '101', '102', '103']
>>> vocabulario[-50:]
['â€˜absorbingâ€™', 'â€˜algorithmâ€™', 'â€˜backwardsâ€™', 'â€˜backâ€™', 'â€˜boldâ€™', 'â€˜bouncingâ€™', 'â€˜bungee-jumpableâ€™', 'â€˜chasingâ€™', 'â€˜derigâ€™', 'â€˜end', 'â€˜enteringâ€™', 'â€˜entersâ€™', 'â€˜enterâ€™', 'â€˜flippingâ€™', 'â€˜followâ€™', 'â€˜forwardsâ€™', 'â€˜gasâ€™', 'â€˜healingâ€™', 'â€˜howâ€™', 'â€˜landingâ€™', 'â€˜liftingâ€™', 'â€˜okayâ€™', 'â€˜oslo', 'â€˜pathâ€™', 'â€˜progressesâ€™', 'â€˜pullingâ€™', 'â€˜reassembleâ€™', 'â€˜reassemblingâ€™', 'â€˜reversingâ€™', 'â€˜risenâ€™', 'â€˜rubensâ€™', 'â€˜scramblingâ€™', 'â€˜shakingâ€™', 'â€˜shovesâ€™', 'â€˜surfingâ€™', 'â€˜swatsâ€™', 'â€˜swatâ€™', 'â€˜targetâ€™', 'â€˜targetâ€™s', 'â€˜tenetâ€™', 'â€˜towardsâ€™', 'â€˜unconsciousâ€™', 'â€˜unpackâ€™', 'â€˜unwedgesâ€™', 'â€˜whatâ€™', 'â€˜whatâ€™s', 'â€˜windfarm', 'â€™', 'â€™em', '“']
>>> tokens[:15]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed-in']
>>> tokens[100:130]
['“', 'The', 'Passenger', 'turns', 'to', 'the', 'back', 'where', 'four', 'BLACK-CLAD', 'YOUNG', 'MEN', 'SIT', ',', 'WAITING', '.', 'The', 'nearest', 'one', 'seems', 'to', 'be', 'SLEEPING', '...', 'PASSENGER', 'Hey', 'â€', '“', 'EYES', 'CLOSED']
>>> palabras[100:130]
['“', 'the', 'passenger', 'turns', 'to', 'the', 'back', 'where', 'four', 'black-clad', 'young', 'men', 'sit', ',', 'waiting', '.', 'the', 'nearest', 'one', 'seems', 'to', 'be', 'sleeping', '...', 'passenger', 'hey', 'â€', '“', 'eyes', 'closed']
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
>>> vocabulario[1:15]
["'d", '(', ')', ',', '-', '.', '...', '/ext', '1', '10', '100', '101', '102', '103']
>>> palabras[100:130]
['“', 'the', 'passenger', 'turns', 'to', 'the', 'back', 'where', 'four', 'black-clad', 'young', 'men', 'sit', ',', 'waiting', '.', 'the', 'nearest', 'one', 'seems', 'to', 'be', 'sleeping', '...', 'passenger', 'hey', 'â€', '“', 'eyes', 'closed']
>>> palabras[1:15]
['written', 'by', 'christopher', 'nolan', 'orchestra', 'tuning', ',', 'audience', 'settling', '.', 'high', 'officials', 'in', 'glassed-in']
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
>>> vocabulario[1:15]
['aback', 'abandoned', 'able', 'about', 'above', 'absolutely', 'accelerate', 'accelerating', 'accelerator', 'access', 'accident', 'accomplished', 'accordioned', 'ace']
>>> len(vocabulario)
3510
>>> len(palabras_crudo)
177437
>>> vocabulario.find('Nolan')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    vocabulario.find('Nolan')
AttributeError: 'list' object has no attribute 'find'
>>> vocabulario.find('aback')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    vocabulario.find('aback')
AttributeError: 'list' object has no attribute 'find'
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> import re
>>> [w for w in vocabulario if re.search('ed$',w)]
['abandoned', 'accomplished', 'accordioned', 'acquired', 'acted', 'agreed', 'amassed', 'angled', 'appeared', 'approached', 'armed', 'asked', 'assigned', 'assured', 'attached', 'attacked', 'authenticated', 'avoided', 'based', 'basked', 'bed', 'bemused', 'blasted', 'bloodshed', 'borrowed', 'bottled', 'bruised', 'buried', 'called', 'carried', 'centred', 'changed', 'cheated', 'claimed', 'closed', 'clouded', 'collapsed', 'coloured', 'committed', 'communicated', 'compared', 'complicated', 'compromised', 'concerned', 'confiscated', 'confused', 'conned', 'convinced', 'copied', 'covered', 'cracked', 'crashed', 'crouched', 'crowded', 'daybed', 'decided', 'defended', 'deserted', 'destroyed', 'detected', 'devastated', 'died', 'distinguished', 'disturbed', 'divided', 'dressed', 'dried', 'dropped', 'drowned', 'dumped', 'dusted', 'embedded', 'emerged', 'enraged', 'entered', 'established', 'estimated', 'estranged', 'examined', 'exhausted', 'expected', 'explained', 'exploded', 'expressed', 'extended', 'failed', 'feed', 'filled', 'financed', 'finished', 'fired', 'flatbed', 'flooded', 'followed', 'forced', 'founded', 'framed', 'frightened', 'frustrated', 'fused', 'gagged', 'gathered', 'glimpsed', 'greed', 'guarded', 'guessed', 'guided', 'handed', 'happened', 'hated', 'healed', 'helped', 'hundred', 'impressed', 'indeed', 'induced', 'inflated', 'informed', 'injured', 'interested', 'interlaced', 'intertwined', 'invented', 'inverted', 'invited', 'involved', 'jagged', 'joined', 'jumped', 'killed', 'learned', 'led', 'licked', 'lied', 'lifted', 'liked', 'lined', 'linked', 'lived', 'located', 'lodged', 'loved', 'magnetized', 'marched', 'marked', 'married', 'merged', 'messed', 'missed', 'monitored', 'moved', 'named', 'need', 'needed', 'nicked', 'nosed', 'noticed', 'notified', 'numbered', 'obliterated', 'opened', 'overwhelmed', 'panicked', 'parked', 'passed', 'pinned', 'planned', 'played', 'pointed', 'polished', 'printed', 'proceed', 'pulled', 'pursued', 'pushed', 'raised', 'realized', 'recruited', 'red', 'reinforced', 'related', 'released', 'relieved', 'renamed', 'rendered', 'repeated', 'repulsed', 'reversed', 'rocked', 'ruined', 'rusted', 'salvaged', 'satisfied', 'saved', 'scarred', 'scored', 'sealed', 'seated', 'secured', 'seemed', 'shipped', 'shocked', 'shouted', 'shoved', 'showed', 'shrivelled', 'silenced', 'singed', 'slipped', 'smashed', 'speed', 'spilled', 'spirited', 'spotted', 'staked', 'started', 'startled', 'stashed', 'strapped', 'stripped', 'studded', 'subtitled', 'succeed', 'sucked', 'supervised', 'supplied', 'supposed', 'surfaced', 'surprised', 'surrounded', 'swapped', 'swiped', 'switched', 'synchronized', 'tailored', 'talked', 'tapped', 'taxed', 'terraced', 'terrified', 'threatened', 'tied', 'tinted', 'tossed', 'towed', 'traced', 'tracked', 'trained', 'transported', 'tried', 'triggered', 'trimmed', 'tripwired', 'turned', 'unaccustomed', 'unacknowledged', 'unauthorized', 'undamaged', 'undetected', 'uniformed', 'unimpeded', 'unmarked', 'unmasked', 'unnoticed', 'unprompted', 'unscheduled', 'used', 'vanished', 'walled', 'wanted', 'warned', 'watched', 'wiped', 'worried', 'wounded', 'wrecked', 'yanked']
>>> [w for w in wordlist if re.search('^..j..t..$',w)]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    [w for w in wordlist if re.search('^..j..t..$',w)]
NameError: name 'wordlist' is not defined
>>> [w for w in vocabulario if re.search('^..j..t..$',w)]
[]
>>> [w for w in vocabulario if re.search('[ghi][mno][jlk][def]$',w)]
['gold', 'hold', 'hole', 'peephole', 'porthole', 'whole']
>>> [w for w in vocabulario if re.search('[mno][mno][mno]',w)]
['afternoon', 'amongst', 'anonymous', 'blooming', 'boom', 'boooom', 'cacophonous', 'cannon', 'chinook', 'chinooks', 'chronology', 'commander', 'commit', 'committed', 'communicate', 'communicated', 'conned', 'demonstrating', 'diamond', 'environment', 'innocent', 'looms', 'moment', 'moments', 'momentum', 'money', 'monitored', 'monitors', 'monopoly', 'monster', 'month', 'months', 'none', 'pandemonium', 'personnel', 'pontoon', 'recommend', 'room', 'rooms', 'salmon', 'soon', 'stateroom', 'tomorrow', 'unnoticed', 'whummmmm', 'zoom', 'zooming', 'zooms']
>>> [w for w in chat_words if re.search('^m+i+n+e+$',w)]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    [w for w in chat_words if re.search('^m+i+n+e+$',w)]
NameError: name 'chat_words' is not defined
>>> [w for w in vocabulario if re.search('^m+i+n+e+$',w)]
['mine']
>>> [w for w in vocabulario if re.search('^[0-9]+\.[0-9+$]',w)]
[]
>>> [w for w in vocabulario if re.search('^[A-Z]',w)]
[]
>>> [w for w in vocabulario if re.search('^[0-9]{4}$',w)]
[]
>>> [w for w in vocabulario if re.search('^[0-9]$',w)]
[]
>>> [w for w in vocabulario if re.search('^[0-9]',w)]
[]
>>> [w for w in vocabulario if re.search('[0-9]',w)]
[]
>>> vocabulario
['a', 'aback', 'abandoned', 'able', 'about', 'above', 'absolutely', 'accelerate', 'accelerating', 'accelerator', 'access', 'accident', 'accomplished', 'accordioned', 'ace', 'achieves', 'acquired', 'across', 'act', 'acted', 'action', 'activates', 'activity', 'actually', 'adds', 'adjusts', 'admire', 'admires', 'advance', 'afar', 'affair', 'affect', 'affixes', 'afraid', 'after', 'afterlife', 'afternoon', 'afterthought', 'afterwards', 'again', 'against', 'age', 'agent', 'ago', 'agreed', 'ahead', 'aim', 'aiming', 'aims', 'air', 'airframe', 'airlock', 'airport', 'alarm', 'alarms', 'algorithm', 'alien', 'alive', 'all', 'alley', 'allies', 'alloys', 'almost', 'alone', 'along', 'alongside', 'already', 'alright', 'also', 'always', 'am', 'amalfi', 'amassed', 'ambition', 'ambulance', 'ambush', 'ambushing', 'american', 'americans', 'ammunition', 'amongst', 'ample', 'an', 'analysis', 'ancestors', 'and', 'andrei', 'anger', 'angled', 'angry', 'anguish', 'animal', 'ankle', 'anna', 'annihilation', 'anonymous', 'another', 'answer', 'answers', 'antagonist', 'antagonists', 'antiaircraft', 'antiques', 'any', 'anyone', 'anything', 'anyway', 'anywhere', 'apart', 'appalling', 'apparatus', 'apparently', 'appear', 'appeared', 'appears', 'appointments', 'appraisal', 'appreciatively', 'approach', 'approached', 'approaches', 'approaching', 'apron', 'archive', 'arcing', 'are', 'area', 'arepo', 'arm', 'armageddon', 'armband', 'armbands', 'armed', 'armour', 'arms', 'around', 'arrangement', 'arrangements', 'arrive', 'arrives', 'arriving', 'art', 'as', 'ashen', 'ashore', 'asia', 'aside', 'ask', 'asked', 'asking', 'asks', 'asphalt', 'assault', 'assembling', 'assess', 'assessing', 'assets', 'assigned', 'assist', 'associate', 'assume', 'assumes', 'assuming', 'assumption', 'assured', 'assuredly', 'at', 'atomic', 'attached', 'attaches', 'attacked', 'attacks', 'attention', 'auction', 'audi', 'audience', 'audio', 'authenticated', 'authentication', 'authority', 'automatic', 'avoid', 'avoided', 'avoiding', 'awake', 'away', 'aye', 'back', 'backing', 'backpack', 'backs', 'backstop', 'backwards', 'bad', 'bag', 'bags', 'balance', 'balconies', 'balcony', 'ball', 'balls', 'bam', 'bang', 'banging', 'bangs', 'banker', 'banking', 'bar', 'barbara', 'bare', 'barely', 'barents', 'bargain', 'barrel', 'barrels', 'barren', 'barriers', 'bars', 'barton', 'base', 'based', 'basic', 'basked', 'bass', 'bathing', 'battle', 'be', 'bean', 'beard', 'bearing', 'bearings', 'beat', 'beaten', 'beautiful', 'became', 'because', 'beckons', 'becomes', 'becoming', 'bed', 'been', 'beep', 'beeps', 'before', 'beg', 'began', 'beginning', 'behind', 'being', 'belief', 'believe', 'believes', 'below', 'belt', 'belts', 'bemused', 'bench', 'beneath', 'benefit', 'bent', 'bentley', 'bern', 'beside', 'best', 'betray', 'betrayal', 'better', 'between', 'beyond', 'bid', 'big', 'bigger', 'billionaire', 'billions', 'binoculars', 'biometric', 'bird', 'birds', 'bitch', 'bite', 'bites', 'bits', 'black', 'blackmail', 'blam', 'blamblamblam', 'bland', 'blank', 'blanket', 'blaring', 'blast', 'blasted', 'blasting', 'blasts', 'blaze', 'blazing', 'bleeding', 'blimey', 'blind', 'blinking', 'block', 'blood', 'bloodshed', 'bloody', 'blooming', 'blossom', 'blow', 'blowing', 'blown', 'blows', 'blue', 'bluetooth', 'bmw', 'board', 'boards', 'boat', 'boats', 'body', 'bodyguards', 'bold', 'bolts', 'bomb', 'bombay', 'bombs', 'booby', 'book', 'books', 'boom', 'boooom', 'boots', 'bore', 'born', 'borrowed', 'boss', 'both', 'bother', 'bothers', 'bottled', 'bottom', 'bought', 'bounce', 'bounces', 'bouncing', 'bound', 'bow', 'bowl', 'box', 'boxes', 'boy', 'brain', 'brake', 'brakes', 'brass', 'breach', 'bread', 'break', 'breakfast', 'breaking', 'breaks', 'breath', 'breathes', 'breathing', 'breathless', 'breaths', 'breezing', 'brick', 'brief', 'briefcase', 'briefcases', 'briefing', 'bring', 'bringing', 'brings', 'british', 'brittle', 'broad', 'broadcast', 'broke', 'broken', 'broker', 'brooks', 'brothers', 'brought', 'bruised', 'brushes', 'brusque', 'buckle', 'buckles', 'budget', 'bug', 'build', 'builder', 'building', 'buildings', 'built', 'bullet', 'bullets', 'bullseye', 'bullshit', 'bumper', 'bungee', 'bunker', 'buried', 'buries', 'burn', 'burning', 'burst', 'bursting', 'bursts', 'bury', 'bus', 'busboys', 'buses', 'business', 'businesses', 'businessman', 'businessmen', 'bustle', 'bustling', 'busy', 'but', 'buttery', 'button', 'buttons', 'buy', 'buying', 'buzzes', 'by', 'cabin', 'cable', 'cacophonous', 'call', 'called', 'calling', 'calls', 'calm', 'came', 'camera', 'camp', 'can', 'cancer', 'canisters', 'cannon', 'capable', 'capsule', 'captain', 'car', 'card', 'cards', 'care', 'carefully', 'carelessly', 'cares', 'cargo', 'carried', 'carries', 'carry', 'carrying', 'cars', 'carving', 'case', 'cash', 'casing', 'casings', 'casually', 'catamaran', 'catapult', 'catch', 'catches', 'catching', 'catering', 'caught', 'cause', 'cavalry', 'cavern', 'centrally', 'centre', 'centred', 'cents', 'centuries', 'certain', 'certainly', 'chain', 'chair', 'chairs', 'chamber', 'chambering', 'chance', 'chances', 'change', 'changed', 'changing', 'chaos', 'charge', 'charm', 'chase', 'chases', 'chasing', 'chatter', 'chatting', 'cheap', 'cheated', 'check', 'checking', 'checks', 'cheek', 'chefs', 'chest', 'chews', 'child', 'childishly', 'chinook', 'chinooks', 'choice', 'chokes', 'choose', 'chop', 'chopper', 'chose', 'christ', 'christopher', 'chronology', 'chuck', 'chunks', 'churning', 'cia', 'cities', 'city', 'civilians', 'claim', 'claimed', 'claiming', 'clanking', 'clarification', 'class', 'classic', 'clattering', 'clean', 'cleaning', 'clear', 'clearance', 'clearly', 'click', 'clicks', 'client', 'clients', 'climate', 'climaxes', 'climb', 'climbing', 'climbs', 'clip', 'clipboard', 'clipping', 'clips', 'clock', 'close', 'closed', 'closely', 'closer', 'closers', 'closes', 'closing', 'clothes', 'cloud', 'clouded', 'clouds', 'club', 'clutching', 'coach', 'coalesces', 'coast', 'coat', 'cock', 'cockpit', 'cocks', 'coffee', 'coin', 'coincidence', 'coke', 'cold', 'collapse', 'collapsed', 'collapses', 'collar', 'colleagues', 'collect', 'collecting', 'collide', 'coloured', 'column', 'coma', 'combination', 'come', 'comes', 'coming', 'commander', 'commit', 'committed', 'communicate', 'communicated', 'company', 'compared', 'compartment', 'complex', 'complicated', 'component', 'components', 'compromise', 'compromised', 'compromising', 'comrades', 'conceive', 'concentrating', 'concern', 'concerned', 'concert', 'concrete', 'concretestructures', 'conducive', 'confiscated', 'conflict', 'confrontation', 'confused', 'congestion', 'conned', 'consciousness', 'consequence', 'consider', 'considers', 'construction', 'cont', 'contact', 'contain', 'container', 'containers', 'containment', 'contemplating', 'contemptuous', 'contents', 'continue', 'continues', 'continuous', 'continuously', 'contract', 'contracting', 'contracts', 'contrite', 'control', 'controlling', 'controls', 'conventional', 'conversation', 'convinced', 'convoy', 'copied', 'copy', 'cord', 'corner', 'corners', 'corpse', 'corresponding', 'corridor', 'cosy', 'cot', 'cotton', 'cough', 'coughing', 'could', 'count', 'countdown', 'counter', 'counting', 'counts', 'couple', 'course', 'court', 'cover', 'covered', 'covering', 'covers', 'cowboy', 'crab', 'crabs', 'crack', 'cracked', 'crackles', 'cracks', 'crash', 'crashed', 'crates', 'crawling', 'creating', 'credit', 'credits', 'creeps', 'crescendos', 'crew', 'crews', 'criminals', 'crosby', 'cross', 'crotch', 'crouched', 'crouches', 'crouching', 'crowbar', 'crowd', 'crowded', 'crunch', 'crushing', 'crystal', 'crystalline', 'cues', 'cuff', 'cufflink', 'cup', 'curdles', 'curious', 'curtains', 'curving', 'cushion', 'customs', 'cut', 'cute', 'cuts', 'cutting', 'cylinder', 'daisy', 'damage', 'danger', 'dangerous', 'dangerously', 'dangle', 'dangling', 'dares', 'daring', 'dark', 'darkness', 'darts', 'date', 'dawn', 'day', 'daybed', 'daylight', 'days', 'dead', 'deafening', 'deal', 'dealer', 'death', 'debris', 'debt', 'decided', 'deciding', 'decision', 'deck', 'decks', 'deduction', 'deep', 'defences', 'defended', 'defiant', 'defraud', 'defuse', 'degrees', 'delaying', 'delivery', 'demonstrating', 'departing', 'department', 'departs', 'depend', 'depot', 'depression', 'depth', 'descend', 'descendants', 'descends', 'deserted', 'desk', 'desolate', 'despair', 'despairing', 'desperate', 'destroy', 'destroyed', 'destroying', 'details', 'detected', 'determination', 'detonation', 'detritus', 'devastated', 'devastating', 'devises', 'diagonal', 'diagram', 'dials', 'diamond', 'did', 'die', 'died', 'dies', 'diet', 'difference', 'different', 'differently', 'digging', 'digs', 'diners', 'dining', 'dinner', 'diplomat', 'direction', 'directions', 'directly', 'dirt', 'disappearing', 'disappears', 'disbelief', 'discreet', 'disembarks', 'dislikes', 'dispassionately', 'displacing', 'display', 'dissipate', 'distance', 'distant', 'distinguish', 'distinguished', 'distortions', 'distract', 'distracting', 'distraction', 'distraught', 'disturbed', 'dive', 'dives', 'divide', 'divided', 'dividing', 'diving', 'do', 'dock', 'dockside', 'doctor', 'document', 'documents', 'dodges', 'dodging', 'does', 'dog', 'doing', 'dollar', 'dollars', 'dollop', 'dolls', 'dominate', 'done', 'door', 'doorman', 'doors', 'doorway', 'dot', 'double', 'down', 'downcast', 'downhill', 'downs', 'downtown', 'dozen', 'dozens', 'dragging', 'drags', 'dramatic', 'draw', 'drawer', 'drawers', 'drawing', 'drawn', 'draws', 'dream', 'dressed', 'dressing', 'dribbling', 'dried', 'dries', 'drilling', 'drink', 'drinking', 'drinks', 'dripping', 'drips', 'drive', 'driven', 'driver', 'drives', 'driving', 'drop', 'dropped', 'dropping', 'drops', 'drown', 'drowned', 'dry', 'duck', 'ducking', 'ducks', 'due', 'dull', 'dumb', 'dumped', 'dusk', 'dust', 'dusted', 'dustily', 'duty', 'dye', 'dying', 'each', 'ear', 'earlier', 'early', 'earpiece', 'earth', 'easiest', 'easing', 'easy', 'eat', 'eating', 'eats', 'echoes', 'edge', 'edges', 'effect', 'efficient', 'efficiently', 'egyptian', 'eight', 'eighteen', 'either', 'ejects', 'elastic', 'elbow', 'eldest', 'electron', 'electronic', 'electronics', 'elegantly', 'elements', 'else', 'elsewhere', 'email', 'embassy', 'embedded', 'embezzler', 'emerge', 'emerged', 'emergency', 'emerges', 'emperor', 'emphatic', 'emplacement', 'empty', 'emts', 'encapsulation', 'encounter', 'end', 'ending', 'endless', 'ends', 'enemy', 'energizing', 'energy', 'enforcement', 'engine', 'engines', 'england', 'english', 'engulfing', 'enjoy', 'enjoying', 'enjoys', 'enormous', 'enough', 'enraged', 'enter', 'entered', 'enters', 'entire', 'entrance', 'entropy', 'environment', 'envy', 'equation', 'equipment', 'erupting', 'escort', 'espresso', 'established', 'establishment', 'estimated', 'estonian', 'estranged', 'europe', 'european', 'evacuate', 'evacuation', 'even', 'evening', 'event', 'eventually', 'ever', 'every', 'everybody', 'everyone', 'everything', 'exact', 'exactly', 'examination', 'examined', 'examines', 'examining', 'exceedingly', 'except', 'exchange', 'exchanges', 'excuse', 'exercises', 'exertion', 'exhausted', 'exist', 'existence', 'exit', 'exits', 'expect', 'expectantly', 'expected', 'expecting', 'expensive', 'experience', 'experiment', 'expertise', 'explain', 'explained', 'explaining', 'explains', 'explode', 'exploded', 'explodes', 'exploding', 'explosion', 'explosive', 'expressed', 'expression', 'ext', 'extended', 'extraction', 'extradition', 'extraordinary', 'eye', 'eyes', 'fabric', 'face', 'faces', 'facilities', 'facility', 'facing', 'factory', 'fade', 'fail', 'failed', 'failure', 'faint', 'fair', 'faith', 'fake', 'fall', 'falling', 'fallow', 'falls', 'familiar', 'family', 'fanatic', 'fanatical', 'far', 'farm', 'farthest', 'fast', 'faster', 'fate', 'favourites', 'fay', 'fear', 'feed', 'feeding', 'feel', 'feeling', 'feels', 'feet', 'feigns', 'fellow', 'felt', 'female', 'fence', 'fencing', 'ferry', 'few', 'feynman', 'fiddling', 'field', 'fifty', 'fight', 'fighting', 'figure', 'file', 'filled', 'fills', 'filthy', 'final', 'finally', 'financed', 'find', 'finding', 'finds', 'fine', 'finger', 'fingers', 'finish', 'finished', 'fire', 'fired', 'firefighter', 'firefighters', 'fireproof', 'fires', 'firing', 'first', 'fishtailing', 'fissile', 'fission', 'fist', 'fists', 'fitness', 'five', 'fixes', 'flame', 'flames', 'flaming', 'flapping', 'flare', 'flashing', 'flat', 'flatbed', 'flattening', 'flew', 'flexes', 'flicker', 'flickering', 'flies', 'flinches', 'flings', 'flips', 'flood', 'flooded', 'floodlit', 'floor', 'flow', 'flown', 'flows', 'fly', 'flying', 'foam', 'foaming', 'focus', 'focuses', 'folding', 'follow', 'followed', 'following', 'follows', 'folly', 'food', 'fool', 'foot', 'for', 'force', 'forced', 'forces', 'forcing', 'forehead', 'forgery', 'forgetting', 'forgive', 'form', 'formation', 'former', 'forming', 'formula', 'forth', 'fortunes', 'forty', 'forward', 'forwards', 'found', 'founded', 'fountain', 'four', 'fragments', 'frame', 'framed', 'frames', 'franks', 'frederick', 'free', 'freedom', 'freeport', 'freeports', 'freezes', 'freezing', 'freight', 'fresh', 'friction', 'friend', 'friendliness', 'friendly', 'friends', 'friendship', 'frightened', 'frisks', 'from', 'front', 'frost', 'frowning', 'frowns', 'frozen', 'frustrated', 'fuck', 'fucking', 'fuel', 'full', 'fully', 'fumbles', 'fumbling', 'fuming', 'function', 'functioning', 'funds', 'furiously', 'further', 'fused', 'fuselage', 'future', 'futures', 'gagged', 'gallery', 'galley', 'games', 'gap', 'garden', 'gas', 'gasoline', 'gasping', 'gasps', 'gate', 'gates', 'gather', 'gathered', 'gathering', 'gathers', 'gaunt', 'gave', 'gaze', 'gear', 'gears', 'geiger', 'generally', 'generation', 'generations', 'gentlemen', 'gently', 'genuine', 'geometrically', 'gesture', 'gestures', 'get', 'gets', 'getting', 'giant', 'gibberish', 'girl', 'give', 'given', 'gives', 'giving', 'glance', 'glances', 'glancing', 'glare', 'glass', 'glaze', 'glimpse', 'glimpsed', 'glittering', 'glove', 'gloves', 'glowing', 'go', 'god', 'goddammit', 'goes', 'going', 'gold', 'golden', 'gon', 'gone', 'good', 'goodbye', 'got', 'gouge', 'government', 'goya', 'gps', 'grab', 'grabbing', 'grabs', 'graceful', 'gracefully', 'grandfather', 'grandpa', 'graphic', 'graphite', 'gratification', 'gratifying', 'grave', 'gravel', 'gravely', 'gravity', 'greasy', 'great', 'greater', 'greatest', 'greed', 'green', 'greet', 'grenade', 'grew', 'grey', 'grinds', 'grinning', 'grins', 'groan', 'groaning', 'groans', 'ground', 'group', 'grubby', 'guarantee', 'guard', 'guarded', 'guarding', 'guards', 'guessed', 'guessing', 'guest', 'guests', 'guided', 'gulp', 'gun', 'gunemplacement', 'gunfire', 'gunpoint', 'gunpowder', 'guns', 'gurgles', 'gurney', 'guy', 'guys', 'had', 'half', 'halfway', 'halide', 'hall', 'halt', 'hammer', 'hand', 'handed', 'handle', 'handling', 'hands', 'hang', 'hangar', 'hanging', 'hangs', 'happen', 'happened', 'happens', 'happy', 'harbour', 'hard', 'hardly', 'harness', 'harnesses', 'harrods', 'has', 'hate', 'hated', 'have', 'havens', 'having', 'havoc', 'hazard', 'he', 'head', 'heading', 'headline', 'heads', 'heal', 'healed', 'health', 'hear', 'hearing', 'hears', 'heart', 'heat', 'heavy', 'heist', 'held', 'helicopter', 'helicopters', 'helipad', 'hell', 'hello', 'helm', 'helmet', 'helmets', 'help', 'helped', 'helping', 'her', 'herculaneum', 'here', 'herself', 'hey', 'hidden', 'hide', 'hides', 'hiding', 'high', 'higher', 'highest', 'highway', 'hill', 'him', 'himself', 'his', 'hisses', 'hissing', 'history', 'hit', 'hitch', 'hits', 'hitting', 'hold', 'holding', 'holds', 'hole', 'holes', 'holiday', 'holocaust', 'holsters', 'home', 'hook', 'hooks', 'hop', 'hope', 'hopeful', 'hoping', 'horizon', 'horn', 'hose', 'hoses', 'hostage', 'hot', 'hotel', 'hour', 'hours', 'house', 'hovers', 'how', 'howling', 'hugs', 'huh', 'hull', 'hum', 'human', 'hundred', 'hung', 'hurls', 'hurries', 'hurt', 'husband', 'hustle', 'hydraulic', 'hydrofoils', 'hyperventilating', 'hypocentre', 'hypothermia', 'i', 'ice', 'icebreaker', 'idea', 'identical', 'identity', 'idling', 'if', 'ignite', 'ignorance', 'ignores', 'imagine', 'imitating', 'immaculately', 'impact', 'impatient', 'implications', 'importance', 'important', 'importing', 'impossible', 'impossibly', 'impregnable', 'impressed', 'improbable', 'in', 'including', 'incoming', 'incomprehensibly', 'increasingly', 'indeed', 'india', 'indian', 'indicates', 'induced', 'industries', 'industry', 'inevitable', 'inflatable', 'inflated', 'information', 'informed', 'injects', 'injured', 'inner', 'innocent', 'inoperable', 'insecure', 'insert', 'inside', 'insist', 'inspect', 'inspection', 'instability', 'instant', 'instantaneous', 'instantly', 'instead', 'instinct', 'instinctively', 'instincts', 'int', 'intact', 'intelligence', 'intending', 'intent', 'intently', 'interest', 'interested', 'interests', 'interfere', 'interior', 'interlaced', 'interlaces', 'interlacing', 'interrogate', 'interrupting', 'intersection', 'intertwined', 'into', 'introduce', 'introduction', 'invented', 'inverse', 'inversion', 'invert', 'inverted', 'inverting', 'inverts', 'investigators', 'investments', 'invited', 'involve', 'involved', 'irate', 'is', 'issue', 'it', 'its', 'itself', 'ives', 'jabs', 'jackknifes', 'jagged', 'jams', 'jaunty', 'jaw', 'jealous', 'jesus', 'jet', 'jewellery', 'jib', 'jibe', 'job', 'join', 'joined', 'joins', 'joke', 'joking', 'journey', 'judgement', 'judging', 'jump', 'jumped', 'jumper', 'jumping', 'jumps', 'junction', 'june', 'junior', 'just', 'kat', 'kate', 'katherine', 'kathy', 'keening', 'keep', 'keeps', 'key', 'keys', 'kick', 'kicking', 'kicks', 'kid', 'kids', 'kiev', 'kill', 'killed', 'killing', 'kills', 'kilo', 'kind', 'king', 'kiss', 'kisses', 'kitchen', 'knee', 'knees', 'knew', 'knife', 'knock', 'knocking', 'knocks', 'know', 'knowing', 'knowledge', 'known', 'knows', 'knuckles', 'laboratory', 'ladder', 'ladders', 'lads', 'lady', 'land', 'landing', 'landmine', 'lands', 'landscape', 'lane', 'lanyard', 'large', 'larger', 'last', 'latches', 'late', 'later', 'laughing', 'laughs', 'launch', 'launches', 'lava', 'law', 'laying', 'lays', 'lazily', 'lead', 'leading', 'leads', 'leafy', 'leaking', 'leaks', 'lean', 'leaning', 'leans', 'leap', 'leaping', 'leaps', 'learned', 'least', 'leather', 'leave', 'leaves', 'leaving', 'lecture', 'led', 'left', 'leftovers', 'leg', 'legal', 'legs', 'length', 'lengths', 'lenses', 'lesion', 'less', 'let', 'lets', 'letting', 'level', 'leverage', 'licked', 'lid', 'lie', 'lied', 'lies', 'life', 'lifelong', 'lift', 'lifted', 'lifting', 'lifts', 'light', 'lighter', 'like', 'liked', 'line', 'linear', 'lined', 'lines', 'lining', 'linked', 'lip', 'lips', 'listen', 'listening', 'listens', 'listings', 'lit', 'little', 'live', 'lived', 'lives', 'living', 'load', 'loading', 'lobby', 'lobs', 'local', 'located', 'location', 'lock', 'lockdown', 'lockpick', 'lockpicks', 'locks', 'locksmiths', 'lodged', 'logistics', 'logjam', 'london', 'long', 'longer', 'look', 'looking', 'looks', 'looms', 'loops', 'loose', 'loosely', 'lose', 'losing', 'loss', 'lost', 'lot', 'loud', 'louder', 'lounge', 'loupe', 'love', 'loved', 'lovely', 'loves', 'low', 'lower', 'lowering', 'lowers', 'loyal', 'luck', 'lucky', 'lump', 'lunch', 'lunges', 'lungfuls', 'lungs', 'lurch', 'luxurious', 'lying', 'lz', 'machine', 'made', 'madman', 'magazine', 'magnetic', 'magnetized', 'magnificent', 'mahir', 'maintaining', 'maintenance', 'majestically', 'make', 'makes', 'making', 'male', 'mall', 'man', 'manage', 'manhattan', 'manufacturing', 'many', 'map', 'maps', 'marched', 'mark', 'marked', 'market', 'markings', 'marks', 'marriage', 'married', 'mars', 'marvelling', 'masculine', 'mask', 'masks', 'mass', 'massive', 'mast', 'material', 'materials', 'matter', 'mattress', 'max', 'may', 'maybe', 'mayhem', 'me', 'meal', 'meals', 'mean', 'meaning', 'means', 'meant', 'meantime', 'meaty', 'mechanics', 'medic', 'medically', 'meet', 'member', 'members', 'membranes', 'memorial', 'men', 'menu', 'mercedes', 'mercy', 'merged', 'mess', 'message', 'messed', 'met', 'metal', 'metallic', 'metals', 'method', 'metres', 'michael', 'microscopic', 'middle', 'might', 'mile', 'millennia', 'million', 'millions', 'mind', 'mine', 'minefield', 'mines', 'mining', 'minute', 'minutes', 'mirror', 'missed', 'misses', 'missile', 'missing', 'mission', 'mistake', 'mixes', 'mixture', 'moaning', 'moans', 'moment', 'moments', 'momentum', 'money', 'monitored', 'monitors', 'monopoly', 'monster', 'month', 'months', 'more', 'morning', 'moscow', 'most', 'mostly', 'mother', 'mothers', 'motion', 'motionless', 'motions', 'mould', 'mouth', 'mouthfuls', 'move', 'moved', 'movement', 'movements', 'moves', 'moving', 'mr', 'mri', 'ms', 'much', 'mud', 'multiple', 'multitude', 'mumbai', 'munitions', 'must', 'my', 'myself', 'na', 'nam', 'name', 'named', 'nanny', 'narrowly', 'nasty', 'national', 'nature', 'near', 'nearby', 'nearest', 'necessary', 'neck', 'need', 'needed', 'needing', 'needs', 'negotiate', 'negotiation', 'neil', 'nervously', 'network', 'never', 'new', 'newly', 'news', 'next', 'nice', 'nick', 'nicked', 'niece', 'night', 'nine', 'ninety', 'no', 'nobody', 'nod', 'nods', 'noise', 'noises', 'nolan', 'none', 'normal', 'norskfreight', 'north', 'northern', 'norway', 'nose', 'nosed', 'not', 'nothing', 'notice', 'noticed', 'notices', 'notified', 'notion', 'now', 'nuclear', 'number', 'numbered', 'numbers', 'numerous', 'nursing', 'nuts', 'obedient', 'object', 'objectives', 'objects', 'obliterated', 'obscure', 'obscuring', 'observe', 'obsessive', 'obvious', 'occurs', 'ocean', 'oceans', 'of', 'off', 'offence', 'offer', 'offering', 'offers', 'office', 'official', 'officials', 'offshore', 'oh', 'okay', 'old', 'older', 'oligarch', 'on', 'once', 'one', 'ones', 'only', 'onto', 'opaque', 'open', 'opened', 'opening', 'opens', 'opera', 'operate', 'operates', 'operating', 'operation', 'operator', 'opinion', 'oppenheimer', 'opposite', 'optimistically', 'option', 'or', 'orange', 'orchestra', 'order', 'ordinance', 'ordinary', 'orient', 'oslo', 'other', 'others', 'our', 'ours', 'ourselves', 'out', 'outer', 'outs', 'outside', 'outskirts', 'over', 'overhead', 'overhears', 'overlooking', 'overnight', 'overwhelmed', 'owe', 'own', 'oxygen', 'pace', 'pack', 'package', 'packing', 'pad', 'padding', 'paid', 'pain', 'painfully', 'paintings', 'pair', 'pal', 'pallet', 'palm', 'pancreatic', 'pandemonium', 'panel', 'panic', 'panicked', 'pans', 'pants', 'paper', 'papers', 'parachute', 'parachuting', 'paradox', 'paramilitaries', 'paramilitary', 'park', 'parked', 'part', 'particles', 'particular', 'partition', 'partner', 'partnership', 'party', 'pass', 'passage', 'passed', 'passenger', 'passengers', 'passes', 'passing', 'passionately', 'passports', 'past', 'patch', 'patches', 'path', 'patient', 'patrol', 'pattern', 'pauses', 'pay', 'paying', 'pays', 'peaking', 'peaks', 'pedestrians', 'peels', 'peephole', 'peering', 'peers', 'pentagon', 'people', 'perfectly', 'perform', 'perimeter', 'person', 'personal', 'personally', 'personnel', 'pessimistically', 'phone', 'physical', 'physics', 'pick', 'pickable', 'picks', 'picture', 'pictures', 'pieces', 'pile', 'pill', 'pillow', 'pills', 'pilots', 'pin', 'pincer', 'pinned', 'pinning', 'pipe', 'pipes', 'pirates', 'pissing', 'pistol', 'pistols', 'pitch', 'place', 'places', 'placing', 'plain', 'plan', 'plane', 'planes', 'planned', 'planning', 'plans', 'planting', 'plastic', 'plate', 'plates', 'platform', 'play', 'played', 'playing', 'plays', 'plaza', 'pleading', 'please', 'pliers', 'plume', 'plutonium', 'pocket', 'pod', 'point', 'pointed', 'pointing', 'points', 'poisoning', 'poles', 'police', 'policeman', 'policemen', 'policy', 'polished', 'polonium', 'pompeii', 'pontoon', 'pooling', 'pop', 'pops', 'population', 'port', 'porthole', 'positron', 'possessions', 'possibility', 'possible', 'possibly', 'posterity', 'pots', 'pour', 'pouring', 'pours', 'power', 'powerboat', 'powers', 'practically', 'practising', 'precariously', 'precautions', 'precise', 'prefer', 'prepare', 'preparing', 'present', 'press', 'pressure', 'presume', 'pretending', 'pretty', 'prevailing', 'prevent', 'previous', 'price', 'primal', 'printed', 'priorities', 'prison', 'private', 'priya', 'probability', 'probably', 'problem', 'procedure', 'proceed', 'prod', 'produce', 'productive', 'profession', 'project', 'projector', 'prominent', 'propagating', 'proper', 'property', 'propose', 'props', 'prosecution', 'protagonist', 'protection', 'protective', 'protein', 'provenance', 'provides', 'proving', 'pry', 'prying', 'puff', 'pull', 'pulled', 'pulling', 'pulls', 'pulse', 'punches', 'pursued', 'pursuit', 'push', 'pushed', 'pushes', 'pushing', 'put', 'puts', 'putting', 'pyramid', 'quarters', 'question', 'questions', 'quiet', 'quietly', 'quite', 'quizzical', 'race', 'races', 'racing', 'racks', 'radiation', 'radio', 'radioactive', 'radius', 'rag', 'rage', 'rages', 'raids', 'rail', 'railing', 'railings', 'rainy', 'raised', 'raises', 'raising', 'rally', 'ramp', 'ran', 'range', 'raps', 'raspberries', 'rather', 'reach', 'reaches', 'reaching', 'react', 'reaction', 'read', 'reader', 'reading', 'ready', 'real', 'realities', 'reality', 'realized', 'realizes', 'realizing', 'really', 'rear', 'reason', 'reassemble', 'reassembles', 'reattaches', 'rebels', 'rebuilt', 'recede', 'receding', 'receiving', 'receptionist', 'recommend', 'record', 'recording', 'recruited', 'red', 'redemption', 'reflective', 'reflexively', 'refuge', 'regains', 'regular', 'reinforced', 'related', 'relationship', 'release', 'released', 'releases', 'relieved', 'remaining', 'remember', 'remnants', 'remote', 'remove', 'removes', 'removing', 'renamed', 'rendered', 'rendering', 'repeat', 'repeated', 'report', 'representative', 'repulsed', 'resign', 'resistance', 'resources', 'respirator', 'respirators', 'response', 'responsible', 'rest', 'restaurant', 'restraining', 'retaken', 'retreat', 'retribution', 'retrospect', 'returns', 'reveal', 'revealing', 'reveals', 'reverse', 'reversed', 'reverses', 'reversing', 'revert', 'revolving', 'ribs', 'ridge', 'rifle', 'rigging', 'right', 'ring', 'ringing', 'rings', 'ringtone', 'rip', 'rips', 'rise', 'rises', 'rising', 'risk', 'risky', 'rivers', 'riyadh', 'road', 'roars', 'robbery', 'rock', 'rocked', 'rocky', 'rods', 'rogue', 'rohan', 'roll', 'roller', 'rolling', 'rolls', 'roof', 'rooftop', 'room', 'rooms', 'rope', 'rose', 'rotas', 'rotate', 'rotors', 'round', 'rounds', 'rover', 'row', 'rpg', 'rubbish', 'rubble', 'rubens', 'ruin', 'ruined', 'ruins', 'rule', 'rumble', 'rumbles', 'rumbling', 'rumour', 'run', 'runaway', 'running', 'runs', 'runway', 'rushes', 'rushing', 'russia', 'russian', 'russians', 'rusted', 'saab', 'safe', 'safety', 'said', 'sail', 'sailing', 'sake', 'salmon', 'salute', 'salvageable', 'salvaged', 'same', 'sample', 'samples', 'sanjay', 'sari', 'sat', 'satellites', 'satisfied', 'sator', 'sators', 'sauce', 'save', 'saved', 'saving', 'savvy', 'saw', 'say', 'saying', 'says', 'scar', 'scarred', 'scars', 'scattering', 'scavenger', 'scene', 'schematic', 'school', 'schoolkids', 'scientist', 'scooping', 'scored', 'scramble', 'scrambles', 'scrambling', 'scrape', 'scream', 'screaming', 'screams', 'screeches', 'screen', 'screws', 'sea', 'seal', 'sealed', 'sealing', 'seals', 'seat', 'seated', 'seats', 'second', 'seconds', 'secret', 'secretary', 'section', 'sections', 'secure', 'secured', 'security', 'sedate', 'sedative', 'seduction', 'seductive', 'see', 'seeing', 'seeking', 'seem', 'seemed', 'seems', 'seen', 'sees', 'seizes', 'self', 'sell', 'selling', 'send', 'sending', 'sends', 'senses', 'sensing', 'sensitive', 'sent', 'sentence', 'separate', 'separates', 'sergeant', 'serious', 'servant', 'service', 'services', 'set', 'sets', 'setting', 'settings', 'settling', 'seventies', 'several', 'sewers', 'shadow', 'shadowing', 'shadows', 'shakes', 'shaking', 'shape', 'share', 'sharp', 'she', 'shearing', 'sheet', 'sheets', 'shell', 'shelter', 'shelters', 'shields', 'shifts', 'ship', 'shipped', 'shipping', 'ships', 'shirt', 'shit', 'shock', 'shocked', 'shocking', 'shoes', 'shoot', 'shooting', 'shoots', 'shopping', 'shore', 'short', 'shot', 'shots', 'should', 'shoulder', 'shoulders', 'shouted', 'shouting', 'shouts', 'shoved', 'shoves', 'shoving', 'show', 'showed', 'shown', 'shows', 'shrapnel', 'shredding', 'shrinks', 'shrivelled', 'shrugs', 'shudder', 'shudders', 'shut', 'shuts', 'siberia', 'side', 'sidearm', 'sides', 'sideways', 'siege', 'sighs', 'sights', 'signal', 'signals', 'silence', 'silenced', 'silencer', 'silent', 'silently', 'sill', 'silly', 'silver', 'similarly', 'simple', 'simultaneously', 'sin', 'singed', 'singh', 'sips', 'sir', 'sirens', 'sit', 'site', 'sits', 'sitting', 'situation', 'sixty', 'size', 'sizing', 'skeptical', 'skidding', 'skids', 'skimming', 'skin', 'sky', 'slamming', 'slams', 'slap', 'slashes', 'sleek', 'sleep', 'sleeping', 'sleeps', 'sleeve', 'slept', 'slicing', 'slide', 'slides', 'sliding', 'slip', 'slipped', 'slippery', 'slipping', 'slips', 'slit', 'slope', 'slotting', 'slow', 'slowing', 'slowly', 'slump', 'slumps', 'smacks', 'small', 'smart', 'smash', 'smashed', 'smashes', 'smashing', 'smears', 'smile', 'smiles', 'smiling', 'smoke', 'smoking', 'smuggling', 'snapping', 'snaps', 'sneers', 'snobbery', 'snow', 'snuck', 'so', 'soda', 'softball', 'soil', 'sold', 'soldier', 'soldiers', 'solid', 'some', 'somebody', 'someone', 'someplace', 'something', 'sometime', 'somewhere', 'son', 'soon', 'sorry', 'sort', 'sorts', 'soul', 'sound', 'sounds', 'soviet', 'space', 'spaniard', 'spar', 'spare', 'sparing', 'sparking', 'sparks', 'speak', 'speaking', 'speaks', 'special', 'specialists', 'specifically', 'speed', 'speedboat', 'speeding', 'speeds', 'spends', 'spilled', 'spilling', 'spin', 'spinning', 'spins', 'spirited', 'spits', 'splinter', 'split', 'splitting', 'spoil', 'spoke', 'sports', 'spot', 'spots', 'spotted', 'spraying', 'sprays', 'spread', 'spring', 'sprinkler', 'sprinklers', 'sprinting', 'squeezes', 'squeezing', 'squirts', 'stabilize', 'stabilizing', 'stabs', 'stack', 'stacks', 'staff', 'stage', 'staircase', 'stairs', 'staked', 'stalls', 'stand', 'standard', 'standing', 'stands', 'stare', 'stares', 'staring', 'start', 'started', 'startled', 'starts', 'stash', 'stashed', 'state', 'stateroom', 'states', 'static', 'station', 'stay', 'steady', 'steal', 'stealing', 'stealthily', 'steam', 'steams', 'steel', 'steely', 'steering', 'steers', 'step', 'stepping', 'steps', 'stern', 'steward', 'stick', 'sticks', 'still', 'stillness', 'stir', 'stop', 'stops', 'stopwatch', 'storage', 'store', 'storeys', 'story', 'straight', 'strange', 'strapped', 'straps', 'streaking', 'stream', 'streaming', 'streams', 'street', 'streets', 'stretcher', 'strikes', 'string', 'strip', 'stripped', 'struck', 'structure', 'structures', 'struggle', 'struggles', 'struggling', 'stuck', 'studded', 'studies', 'study', 'studying', 'stuff', 'stuffs', 'stumbles', 'stupid', 'subside', 'subsidence', 'subtitled', 'subtly', 'suburban', 'succeed', 'such', 'sucked', 'sucking', 'sudden', 'suddenly', 'suffocate', 'suicide', 'suit', 'suits', 'sun', 'sunlight', 'sunscreen', 'sunset', 'sunsets', 'sunshine', 'supertitle', 'supervised', 'supervisor', 'supplied', 'suppose', 'supposed', 'suppress', 'sure', 'surfaced', 'surprise', 'surprised', 'surprises', 'surprisingly', 'surreal', 'surrounded', 'surrounding', 'survival', 'suv', 'suvs', 'swap', 'swapped', 'swaps', 'swarm', 'swat', 'swats', 'swaying', 'sweating', 'sweetly', 'swell', 'swerves', 'swift', 'swiftly', 'swimming', 'swinging', 'swings', 'swiped', 'swirls', 'swiss', 'switch', 'switched', 'switches', 'swore', 'sync', 'synchronized', 'system', 'systems', 'table', 'tackles', 'tactical', 'tail', 'tailor', 'tailored', 'take', 'taken', 'takes', 'taking', 'talisman', 'talk', 'talked', 'talking', 'tall', 'tallinn', 'tangling', 'tape', 'tapped', 'taps', 'target', 'tarmac', 'task', 'taste', 'tasteful', 'taut', 'tax', 'taxed', 'taxiway', 'tea', 'team', 'teams', 'tears', 'tech', 'technology', 'teenager', 'teeth', 'tell', 'telling', 'temporal', 'ten', 'tenant', 'tender', 'tenders', 'tends', 'tenet', 'tenets', 'tensioning', 'tent', 'tentatively', 'term', 'terminal', 'terms', 'terrace', 'terraced', 'terraces', 'terrible', 'terribly', 'terrified', 'terrorism', 'terrorist', 'terrorists', 'test', 'tests', 'text', 'than', 'thanks', 'that', 'the', 'theatre', 'theatrically', 'their', 'theirs', 'them', 'themselves', 'then', 'theory', 'there', 'these', 'they', 'thickens', 'thin', 'thing', 'things', 'think', 'thinking', 'thinks', 'third', 'this', 'those', 'though', 'thought', 'thousand', 'thread', 'threat', 'threatened', 'three', 'throat', 'throng', 'through', 'throw', 'throwing', 'thrown', 'throws', 'thrust', 'thrusting', 'thrusts', 'thud', 'thug', 'thugs', 'thumb', 'thundering', 'thursday', 'tick', 'ticket', 'tie', 'tied', 'ties', 'tiger', 'tight', 'tightens', 'time', 'timers', 'times', 'tinted', 'tiny', 'tips', 'to', 'toast', 'today', 'together', 'told', 'tomas', 'tomb', 'tomorrow', 'tonic', 'tonight', 'too', 'took', 'tool', 'tools', 'top', 'tops', 'tossed', 'tosses', 'tossing', 'touch', 'tough', 'tour', 'tourists', 'towards', 'towed', 'tower', 'towers', 'town', 'towns', 'traced', 'tracked', 'tracker', 'tracking', 'tracks', 'trade', 'traffic', 'trails', 'train', 'trained', 'training', 'trains', 'traitor', 'tram', 'transcends', 'transfer', 'transit', 'transitions', 'transmits', 'transponder', 'transport', 'transportation', 'transported', 'trap', 'trappings', 'travel', 'travelling', 'travels', 'tray', 'treacherous', 'treasury', 'treat', 'trembling', 'trickle', 'tried', 'tries', 'trieste', 'trigger', 'triggered', 'triggers', 'trimmed', 'trips', 'tripwire', 'tripwired', 'trondheim', 'troops', 'truck', 'trucks', 'true', 'trunk', 'trust', 'truth', 'try', 'trying', 'tube', 'tugs', 'tumblers', 'tumbles', 'tumbling', 'tuning', 'tunnel', 'tunnels', 'turbine', 'turbines', 'turn', 'turned', 'turning', 'turns', 'turnstile', 'tutor', 'twenty', 'twice', 'twilight', 'twitches', 'two', 'type', 'tyre', 'tyres', 'ukraine', 'ukrainian', 'ukrainians', 'unacceptable', 'unaccustomed', 'unacknowledged', 'unafraid', 'unauthorized', 'unbroken', 'unclip', 'unclips', 'unconscious', 'undamaged', 'under', 'underground', 'underneath', 'understand', 'undetected', 'unearthing', 'uneasy', 'unexpectedly', 'unexplodes', 'unfolds', 'uniform', 'uniformed', 'unimpeded', 'uninvent', 'union', 'unique', 'unison', 'unit', 'units', 'universe', 'unknowable', 'unless', 'unlike', 'unlock', 'unmarked', 'unmasked', 'unnoticed', 'unplugs', 'unpredictable', 'unprompted', 'unroll', 'unscheduled', 'unscrews', 'unseen', 'unsplashing', 'untie', 'until', 'unusual', 'unzips', 'up', 'upper', 'upside', 'upstream', 'upwards', 'urgent', 'urging', 'us', 'use', 'used', 'useless', 'uses', 'ushers', 'using', 'usually', 'utility', 'utterly', 'vacantly', 'valuation', 'value', 'van', 'vanish', 'vanished', 'vanishes', 'variety', 'vast', 'vault', 'vaults', 'vehicle', 'vehicles', 'velcro', 'vengeful', 'vents', 'verify', 'version', 'vertiginous', 'very', 'vest', 'vests', 'via', 'vibrate', 'viciousness', 'viet', 'view', 'violate', 'violently', 'vision', 'visit', 'visiting', 'vodka', 'voice', 'voicemail', 'voices', 'volkov', 'vouch', 'vulnerable', 'waistband', 'wait', 'waiter', 'waiting', 'waits', 'wake', 'wakes', 'walk', 'walking', 'walks', 'wall', 'walled', 'walls', 'want', 'wanted', 'wanting', 'wants', 'war', 'warehouses', 'warhead', 'warm', 'warn', 'warned', 'warning', 'wary', 'was', 'washing', 'watch', 'watched', 'watches', 'watching', 'water', 'wave', 'waves', 'way', 'ways', 'we', 'wealthy', 'weapon', 'weaponry', 'weapons', 'wear', 'wearing', 'wears', 'weaving', 'wedges', 'week', 'weeks', 'weight', 'welcome', 'well', 'welling', 'went', 'were', 'west', 'wet', 'wets', 'wham', 'what', 'whatever', 'wheel', 'wheeler', 'wheeling', 'wheels', 'when', 'where', 'whether', 'which', 'whiff', 'while', 'whimper', 'whine', 'whirl', 'whisper', 'whispers', 'white', 'whitman', 'who', 'whoa', 'whole', 'whose', 'whummmmm', 'why', 'wife', 'wiggling', 'will', 'willing', 'winces', 'winch', 'winches', 'wind', 'windbreaker', 'windmill', 'window', 'windows', 'windpipe', 'windshield', 'windswept', 'wine', 'wing', 'wings', 'wiped', 'wipes', 'wire', 'wisps', 'with', 'within', 'without', 'woken', 'woman', 'women', 'won', 'wood', 'wooden', 'word', 'work', 'worker', 'workers', 'working', 'works', 'world', 'worlds', 'worried', 'worry', 'worse', 'worst', 'worth', 'would', 'wound', 'wounded', 'wow', 'wraps', 'wreaking', 'wreck', 'wrecked', 'wrecker', 'wrist', 'written', 'wrong', 'yacht', 'yachts', 'yanked', 'yanks', 'yard', 'yards', 'yeah', 'year', 'years', 'yellow', 'yes', 'yet', 'yoga', 'you', 'young', 'your', 'yours', 'yourself', 'yourselves', 'yup', 'zero', 'zip', 'zips', 'zone', 'zoom', 'zooming', 'zooms']
>>> [w for w in tokens if re.search('[0-9]',w)]
['2', '3', 'â\x80\x984:23â\x80\x99', 'â\x80\x984:22â\x80\x99', '2', '4', '3', '2', '2', '2', '3', 'â\x80\x981:58â\x80\x99', 'â\x80\x981:57â\x80\x99', 'â\x80\x980:34â\x80\x99', 'â\x80\x980:33â\x80\x99', 'â\x80\x980:32â\x80\x99', 'â\x80\x980:31â\x80\x99', '5.', 'â\x80\x980:03â\x80\x99', '6', '7', 'â\x80\x985:38â\x80\x99', 'â\x80\x986:53â\x80\x99', '7', '8', '9', '10', 'B-2â\x80\x99', 'B-2', '11', '25m', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', 'Stalsk-12', '24', '200,000', 'Stalsk-12', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '2', '45', '46', '2', '47', '48', '49', '50', '51', '241', '241', '241', '52', '241', '53', '29th', '7', '7:30', '54', '70', '55', '56', '57', '58', '59', '2008', '241', '241', '14th', '60', '61', '62', '63', '241', 'Stalsk-12', '64', '241â\x80\x99s', '65', '66', '67', '68', '69', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '4', '5', '92', '93', '94', '95', '96', '130', '97', '98', '241', '99', '100', '101', '102', '103', '104', '105', '2', '106', '107', '241', '241', '108', '241', '109', '241', '110', '111', '112', '113', '114', '14th', '115', '14th', 'Stalsk-12', '14th', '116', '14th', '117', '118', 'Stalsk-12', '1', '2', '119', '1', '120', '2', 'â\x80\x9810â\x80\x99', 'â\x80\x9810â\x80\x99', '1', '121', '122', 'Stalsk-12', 'STALSK-12', 'STALSK-12', 'STALSK-12', 'STALSK-12', '123', 'â\x80\x989:59â\x80\x99', 'â\x80\x989:58â\x80\x99', 'STALSK-12', 'â\x80\x989:57â\x80\x99', 'â\x80\x989:56â\x80\x99', '124', 'STALSK-12', 'STALSK-12', 'STALSK-12', '125', 'â\x80\x988:10â\x80\x99', 'â\x80\x988:09â\x80\x99', 'STALSK-12', 'â\x80\x988:08â\x80\x99', 'â\x80\x988:07â\x80\x99', '126', 'STALSK-12', 'STALSK-12', 'â\x80\x986:24â\x80\x99', 'â\x80\x986:23â\x80\x99', 'STALSK-12', 'â\x80\x985:15â\x80\x99', 'â\x80\x985:14â\x80\x99', '127', 'â\x80\x985:10â\x80\x99', 'â\x80\x985:09â\x80\x99', 'â\x80\x985:04â\x80\x99', 'â\x80\x985:03â\x80\x99', 'STALSK-12', 'â\x80\x985:01â\x80\x99', 'â\x80\x985:00â\x80\x99', '128', 'STALSK-12', 'STALSK-12', 'STALSK-12', 'STALSK-12', '129', 'STALSK-12', 'STALSK-12', 'MI8', '130', 'â\x80\x984:10â\x80\x99', 'â\x80\x984:09â\x80\x99', 'STALSK-12', 'â\x80\x984:06â\x80\x99', 'â\x80\x984:05â\x80\x99', '131', 'STALSK-12', 'STALSK-12', '132', '183', 'STALSK-12', 'â\x80\x982:12â\x80\x99', 'â\x80\x982:11â\x80\x99', '133', 'STALSK-12', 'STALSK-12', 'STALSK-12', '134', 'STALSK-12', '135', 'STALSK-12', 'STALSK-12', 'â\x80\x981:07â\x80\x99', 'â\x80\x981:06â\x80\x99', 'STALSK-12', '136', '137', 'STALSK-12', 'STALSK-12', '138', '139', 'STALSK-12', 'STALSK-12', 'â\x80\x9800:09â\x80\x99', 'â\x80\x9800:08â\x80\x99', 'STALSK-12', 'STALSK-12', '140', 'STALSK-12', '141', 'STALSK-12', 'Stalsk-12', '142', '143', '144', '145', '3', '3', '146', '147']
>>> [w for w in vocabulario if re.search('(ed|ing)$',w)]

>>> [w for w in vocabulario if re.search('(ed|ing)$',w)][:10]
['abandoned', 'accelerating', 'accomplished', 'accordioned', 'acquired', 'acted', 'agreed', 'aiming', 'amassed', 'ambushing']
>>> [w for w in vocabulario if re.search('ed|ing$',w)][:10]
['abandoned', 'accelerating', 'accomplished', 'accordioned', 'acquired', 'acted', 'agreed', 'aiming', 'amassed', 'ambushing']
>>> fd = nltk.FreqDist(vs for word in wsj
			  for vs in re.findall(r'[aeiou]{2,}', word))
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    fd = nltk.FreqDist(vs for word in wsj
NameError: name 'wsj' is not defined
>>> fd = nltk.FreqDist(vs for word in vocabulario
			  for vs in re.findall(r'[aeiou]{2,}', word))
>>> 
>>> fd.most_common(12)
[('ea', 212), ('ou', 108), ('io', 104), ('ai', 94), ('ee', 88), ('ie', 87), ('oo', 63), ('ia', 38), ('oa', 31), ('au', 31), ('oi', 26), ('ui', 25)]
>>> [int(n) for n in re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    [int(n) for n in re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
  File "<pyshell#43>", line 1, in <listcomp>
    [int(n) for n in re.findall('[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall('[0-9]{4}\-[0-9]{2}\-[0-9]{2}','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    [int(n) for n in re.findall('[0-9]{4}\-[0-9]{2}\-[0-9]{2}','2009-12-31')]
  File "<pyshell#44>", line 1, in <listcomp>
    [int(n) for n in re.findall('[0-9]{4}\-[0-9]{2}\-[0-9]{2}','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    [int(n) for n in re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
  File "<pyshell#45>", line 1, in <listcomp>
    [int(n) for n in re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall(r'[0-9]','2009-12-31')]
[2, 0, 0, 9, 1, 2, 3, 1]
>>> [int(n) for n in re.findall(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    [int(n) for n in re.findall(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$','2009-12-31')]
  File "<pyshell#47>", line 1, in <listcomp>
    [int(n) for n in re.findall(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall(r'^[0-9]+-[0-9]+-[0-9]+$','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    [int(n) for n in re.findall(r'^[0-9]+-[0-9]+-[0-9]+$','2009-12-31')]
  File "<pyshell#48>", line 1, in <listcomp>
    [int(n) for n in re.findall(r'^[0-9]+-[0-9]+-[0-9]+$','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall('[0-9]+-[0-9]+-[0-9]+','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    [int(n) for n in re.findall('[0-9]+-[0-9]+-[0-9]+','2009-12-31')]
  File "<pyshell#49>", line 1, in <listcomp>
    [int(n) for n in re.findall('[0-9]+-[0-9]+-[0-9]+','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-12-31'
>>> [int(n) for n in re.findall('[0-9]+-+','2009-12-31')]
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    [int(n) for n in re.findall('[0-9]+-+','2009-12-31')]
  File "<pyshell#50>", line 1, in <listcomp>
    [int(n) for n in re.findall('[0-9]+-+','2009-12-31')]
ValueError: invalid literal for int() with base 10: '2009-'
>>> [int(n) for n in re.findall('[0-9]+','2009-12-31')]
[2009, 12, 31]
>>> regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'
>>> def compress(word):
	pieces = re.findall(regexp, word)
	return ''.join(pieces)

>>> print(nltk.tokenwrap(compress(w) for w in vocabulario[:50]))
a abck abndnd able abt abve absltly acclrte acclrtng acclrtr accss
accdnt accmplshd accrdnd ace achvs acqrd acrss act actd actn actvts
actvty actlly adds adjsts admre admrs advnce afr affr affct affxs afrd
aftr aftrlfe aftrnn aftrthght aftrwrds agn agnst age agnt ago agrd ahd
aim aimng aims air
>>> print(nltk.tokenwrap(compress(w) for w in tokens[:50]))
TNT Wrttn by Chrstphr Nln ORCHSTRA TNNG , audnce sttlng . Hgh offcls
in glssd-n bxs tst each othr . Drs clsng ... BM â frm bhnd the
orchstra â TRRRSTS wth MCHNE GNS BRST in ... The audnce SCRMS ...
The trrrsts cvr the ordnry pple â the HGH
>>> cvs = [cv for w in vocabulario for cv in re.findall(r'[ptksvr][aeiou]',w)]
>>> cfd = nltk.ConditionalFreqDist(cvs)
>>> cfd.tabulate
<bound method ConditionalFreqDist.tabulate of <ConditionalFreqDist with 6 conditions>>
>>> cfd.tabulate()
    a   e   i   o   u 
k   8  71  57   2   0 
p  90 111  57  76  19 
r 194 312 187 153  50 
s  39 192 126  41  58 
t 125 249 233  79  50 
v  25 152  47  16   1 
>>> cv_word_pairs = [(cv, w) for w in rotokas_words
			     for cv in re.findall(regexp, w)]
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    cv_word_pairs = [(cv, w) for w in rotokas_words
NameError: name 'rotokas_words' is not defined
>>> cv_word_pairs = [(cv, w) for w in tokens
			     for cv in re.findall(regexp, w)]
>>> cv_word_pairs = [(cv, w) for w in vocabulario
			     for cv in re.findall(regexp, w)]
>>> cv_index = nltk.Index(cv_word_pairs)
>>> cv_index['su']
[]
>>> cv_word_pairs = [(cv, w) for w in vocabulario
			     for cv in re.findall(r'[ptksvr][aeiou]', w)]
>>> cv_index = nltk.Index(cv_word_pairs)
>>> cv_index['su']
['assume', 'assumes', 'assuming', 'assumption', 'assured', 'assuredly', 'capsule', 'casually', 'encapsulation', 'issue', 'jesus', 'pressure', 'presume', 'pursued', 'pursuit', 'subside', 'subsidence', 'subtitled', 'subtly', 'suburban', 'succeed', 'such', 'sucked', 'sucking', 'sudden', 'suddenly', 'suffocate', 'suicide', 'suit', 'suits', 'sun', 'sunlight', 'sunscreen', 'sunset', 'sunsets', 'sunshine', 'supertitle', 'supervised', 'supervisor', 'supplied', 'suppose', 'supposed', 'suppress', 'sure', 'surfaced', 'surprise', 'surprised', 'surprises', 'surprisingly', 'surreal', 'surrounded', 'surrounding', 'survival', 'suv', 'suvs', 'treasury', 'unusual', 'usually']
>>> cv_index['vo']
['avoid', 'avoided', 'avoiding', 'convoy', 'favourites', 'havoc', 'involve', 'involved', 'nervously', 'revolving', 'vodka', 'voice', 'voicemail', 'voices', 'volkov', 'vouch']
>>> cv_index['vu']
['vulnerable']
>>> cv_index['ka']
['kat', 'kate', 'katherine', 'kathy', 'okay', 'package', 'pickable', 'vodka']
>>> def stem(word):
	for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
		if word.endswith(suffix):
			return word[:-len(suffix)]
		return word

	
>>> re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['ing']
>>> re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['processing']
>>> re.findall(r'^(.*)(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
['process']
>>> re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
[('process', 'ing')]
>>> re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')
[('process', 'ing')]
>>> def stem(word):
	regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
	stem, suffix = re.findall(regexp, word)[0]
	return stem

>>> [stem(t) for t in tokens[:15]]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    [stem(t) for t in tokens[:15]]
  File "<pyshell#90>", line 1, in <listcomp>
    [stem(t) for t in tokens[:15]]
  File "<pyshell#89>", line 3, in stem
    stem, suffix = re.findall(regexp, word)[0]
IndexError: list index out of range
>>> [stem(t) for t in tokens]
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    [stem(t) for t in tokens]
  File "<pyshell#91>", line 1, in <listcomp>
    [stem(t) for t in tokens]
  File "<pyshell#89>", line 3, in stem
    stem, suffix = re.findall(regexp, word)[0]
IndexError: list index out of range
>>> def stem(word):
	regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
	stem, suffix = re.findall(regexp, word)
	return stem

>>> [stem(t) for t in tokens[:15]]
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    [stem(t) for t in tokens[:15]]
  File "<pyshell#94>", line 1, in <listcomp>
    [stem(t) for t in tokens[:15]]
  File "<pyshell#93>", line 3, in stem
    stem, suffix = re.findall(regexp, word)
ValueError: not enough values to unpack (expected 2, got 0)
>>> def stem(word):
	regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$'
	stem, suffix = re.findall(regexp, word)[0]
	return stem

>>> [stem(t) for t in vocabulario[:15]]
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    [stem(t) for t in vocabulario[:15]]
  File "<pyshell#97>", line 1, in <listcomp>
    [stem(t) for t in vocabulario[:15]]
  File "<pyshell#96>", line 3, in stem
    stem, suffix = re.findall(regexp, word)[0]
IndexError: list index out of range
>>> vocabulario.findall(r'<a>(<.*>)<man>')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    vocabulario.findall(r'<a>(<.*>)<man>')
AttributeError: 'list' object has no attribute 'findall'
>>> tokens.findall(r'<a>(<.*>)<man>')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    tokens.findall(r'<a>(<.*>)<man>')
AttributeError: 'list' object has no attribute 'findall'
>>> vocabulario[:20]
['a', 'aback', 'abandoned', 'able', 'about', 'above', 'absolutely', 'accelerate', 'accelerating', 'accelerator', 'access', 'accident', 'accomplished', 'accordioned', 'ace', 'achieves', 'acquired', 'across', 'act', 'acted']
>>> tokens[:20]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed-in', 'boxes', 'toast', 'each', 'other', '.']
>>> tokens.findall(r"<a> (<.*>) <man>")
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    tokens.findall(r"<a> (<.*>) <man>")
AttributeError: 'list' object has no attribute 'findall'
>>> palabras_crudo.findall(r"<a> (<.*>) <man>")
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    palabras_crudo.findall(r"<a> (<.*>) <man>")
AttributeError: 'str' object has no attribute 'findall'
>>> nltk.Text(tokens).findall(r"<a> (<.*>) <man>")
hard
>>> nltk.Text(tokens).findall(r"<.*> <.*> <bro>")

>>> nltk.Text(tokens).findall(r"<1.*>{3,}")

>>> nltk.Text(tokens).findall(r"<l.*>{3,}")

>>> nltk.Text(tokens).nltk.app.nemo(r"ied$")
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    nltk.Text(tokens).nltk.app.nemo(r"ied$")
AttributeError: 'Text' object has no attribute 'nltk'
>>> tokens.nltk.app.nemo(r"ied$")
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    tokens.nltk.app.nemo(r"ied$")
AttributeError: 'list' object has no attribute 'nltk'
>>> nltk.re_show(r'ied$', palabras_crudo)

>>> nltk.re_show(r'ied$', palabras_crudo)[:10]

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    nltk.re_show(r'ied$', palabras_crudo)[:10]
TypeError: 'NoneType' object is not subscriptable
>>> porter = nltk.PorterStemmer()
>>> lancaster = nltk.LancasterStemmer()
>>> [porter.stem(t) for t in tokens[:25]]
['tenet', 'written', 'by', 'christoph', 'nolan', 'orchestra', 'tune', ',', 'audienc', 'settl', '.', 'high', 'offici', 'in', 'glassed-in', 'box', 'toast', 'each', 'other', '.', 'door', 'close', '...', 'bam', 'â\x80\x93']
>>> [lancaster.stem(t) for t in tokens[:25]]
['tenet', 'writ', 'by', 'christopher', 'nol', 'orchestr', 'tun', ',', 'audy', 'settl', '.', 'high', 'off', 'in', 'glassed-in', 'box', 'toast', 'each', 'oth', '.', 'door', 'clos', '...', 'bam', 'â\x80\x93']
>>> wnl = nltk.WordNetLemmatizer()
>>> [wnl.stem(t) for t in tokens[:25]]
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    [wnl.stem(t) for t in tokens[:25]]
  File "<pyshell#117>", line 1, in <listcomp>
    [wnl.stem(t) for t in tokens[:25]]
AttributeError: 'WordNetLemmatizer' object has no attribute 'stem'
>>> [wnl.lemmatize(t) for t in tokens[:25]]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'official', 'in', 'glassed-in', 'box', 'toast', 'each', 'other', '.', 'Doors', 'closing', '...', 'BAM', 'â\x80\x93']
>>> re.split(r' ', palabras_crudo[:25])
['TENET\nWritten', 'by\nChristop']
>>> re.split(r' ', palabras_crudo[:200])
['TENET\nWritten', 'by\nChristopher', 'Nolan\nORCHESTRA', 'TUNING,', 'audience', 'settling.', 'High', 'officials', 'in', '\nglassed-in', 'boxes', 'toast', 'each', 'other.', 'Doors', 'closing...\nBAM', 'â\x80\x93', 'from', 'behind', 'the', 'orchestra', 'â\x80\x93', 'TERRORISTS', 'with', 'MAC']
>>> re.split(r'[ \t\n+]', palabras_crudo[:200])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING,', 'audience', 'settling.', 'High', 'officials', 'in', '', 'glassed-in', 'boxes', 'toast', 'each', 'other.', 'Doors', 'closing...', 'BAM', 'â\x80\x93', 'from', 'behind', 'the', 'orchestra', 'â\x80\x93', 'TERRORISTS', 'with', 'MAC']
>>> re.split(r'\s+', palabras_crudo[:200])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING,', 'audience', 'settling.', 'High', 'officials', 'in', 'glassed-in', 'boxes', 'toast', 'each', 'other.', 'Doors', 'closing...', 'BAM', 'â\x80\x93', 'from', 'behind', 'the', 'orchestra', 'â\x80\x93', 'TERRORISTS', 'with', 'MAC']
>>> print((re.split(r'\s+', palabras_crudo[:200])).encode('unicode_escape'))
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    print((re.split(r'\s+', palabras_crudo[:200])).encode('unicode_escape'))
AttributeError: 'list' object has no attribute 'encode'
>>> re.split(r'\W+', palabras_crudo)

>>> re.split(r'\W+', palabras_crudo[:20])
['TENET', 'Written', 'by', 'Chr']
>>> re.split(r'\W+', palabras_crudo[:200])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', 'audience', 'settling', 'High', 'officials', 'in', 'glassed', 'in', 'boxes', 'toast', 'each', 'other', 'Doors', 'closing', 'BAM', 'â', 'from', 'behind', 'the', 'orchestra', 'â', 'TERRORISTS', 'with', 'MAC']
>>> re.split(r'\w+|\S\w*', palabras_crudo[:200])
['', '\n', ' ', '\n', ' ', '\n', ' ', '', ' ', ' ', '', ' ', ' ', ' ', ' \n', '', ' ', ' ', ' ', ' ', '', ' ', ' ', '', '', '', '\n', ' ', '', '', ' ', ' ', ' ', ' ', ' ', '', '', ' ', ' ', ' ', '']
>>> re.split(r'\w+|\S\w*', palabras_crudo[:300])
['', '\n', ' ', '\n', ' ', '\n', ' ', '', ' ', ' ', '', ' ', ' ', ' ', ' \n', '', ' ', ' ', ' ', ' ', '', ' ', ' ', '', '', '', '\n', ' ', '', '', ' ', ' ', ' ', ' ', ' ', '', '', ' ', ' ', ' ', ' \n', ' ', ' ', '', '', '', ' ', ' ', ' ', '', '', '', ' ', ' ', ' ', ' \n', ' ', ' ', ' ', '', '', ' ', ' ', '']
>>> re.findall(r'\w+|\S\w*', palabras_crudo[:30])
['TENET', 'Written', 'by', 'Christopher', 'N']
>>> re.findall(r'\w+|\S\w*', palabras_crudo[:100])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed', '-i']
>>> re.findall(r'\w+|\S\w*', palabras_crudo[:500])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed', '-in', 'boxes', 'toast', 'each', 'other', '.', 'Doors', 'closing', '.', '.', '.', 'BAM', 'â', '\x80', '\x93', 'from', 'behind', 'the', 'orchestra', 'â', '\x80', '\x93', 'TERRORISTS', 'with', 'MACHINE', 'GUNS', 'BURST', 'in', '.', '.', '.', 'The', 'audience', 'SCREAMS', '.', '.', '.', 'The', 'terrorists', 'cover', 'the', 'ordinary', 'people', 'â', '\x80', '\x93', 'the', 'HIGH', 'OFFICIALS', 'are', 'held', 'in', 'the', 'BOXES', '.', '.', '.', 'INT', '.', '/EXT', '.', 'VAN', ',', 'PLAZA', ',', 'DOWNTOWN', 'KIEV', ',', 'UKRAINE', 'â', '\x80', '\x93', 'DAY', 'As', 'POLICE', 'FLOOD', 'THE', 'PLAZA', ',', 'the', 'DRIVER', 'turns', 'to', 'the', 'PASSENGER', 'â', '\x80', '\x93', 'DRIVER', '(in', 'Ukrainian', ')', 'â', '\x80', '\x93', 'Wake', 'up', 'the', 'Ameri']
>>> re.findall(r'\', palabras_crudw+(?:[-']\w+)*|'|[-.(]+|\S\w*']o[:500])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> re.findall(r'\', palabras_crudw+(?:[-')\w+)*|'|[-.(]+|\S\w*']o[:500])
SyntaxError: unexpected character after line continuation character
>>> re.findall(r'\w+(?:[-']\w+)*|'|[-.(]+|\S\w*']', palabras_crudo[:500]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*"]', palabras_crudo[:500]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", palabras_crudo[:500])
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed-in', 'boxes', 'toast', 'each', 'other', '.', 'Doors', 'closing', '...', 'BAM', 'â', '\x80', '\x93', 'from', 'behind', 'the', 'orchestra', 'â', '\x80', '\x93', 'TERRORISTS', 'with', 'MACHINE', 'GUNS', 'BURST', 'in', '...', 'The', 'audience', 'SCREAMS', '...', 'The', 'terrorists', 'cover', 'the', 'ordinary', 'people', 'â', '\x80', '\x93', 'the', 'HIGH', 'OFFICIALS', 'are', 'held', 'in', 'the', 'BOXES', '...', 'INT', '.', '/EXT', '.', 'VAN', ',', 'PLAZA', ',', 'DOWNTOWN', 'KIEV', ',', 'UKRAINE', 'â', '\x80', '\x93', 'DAY', 'As', 'POLICE', 'FLOOD', 'THE', 'PLAZA', ',', 'the', 'DRIVER', 'turns', 'to', 'the', 'PASSENGER', 'â', '\x80', '\x93', 'DRIVER', '(', 'in', 'Ukrainian', ')', 'â', '\x80', '\x93', 'Wake', 'up', 'the', 'Ameri']
>>> pattern = r'''(?x)          #set flag to allow verbose regexps
		(?:[A-Z]\.)+	#abbreviations, e.g. U.S.A.
		| \w+(?:\w+)*	#words with optional integral hyphens
		| \$?\d+(?;\.\d+)?%?	#currency and percentages, e.g. $12.40, 82%
		| \.\.\.	#elipsis
		| [][.,;"'?():-_`] #there are separate tokens; includes ], [ '''
>>> nltk.regexp_tokenize(palabras_crudo, pattern)[:50]
Traceback (most recent call last):
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 817, in _parse
    raise Verbose
sre_parse.Verbose

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    nltk.regexp_tokenize(palabras_crudo, pattern)[:50]
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 216, in regexp_tokenize
    return tokenizer.tokenize(text)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 123, in tokenize
    self._check_regexp()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 120, in _check_regexp
    self._regexp = re.compile(self._pattern, self._flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\re.py", line 252, in compile
    return _compile(pattern, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 956, in parse
    p = _parse_sub(source, state, True, 0)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 823, in _parse
    raise source.error("unknown extension ?" + char,
re.error: unknown extension ?; at position 157 (line 4, column 12)
>>> nltk.regexp_tokenize(palabras_crudo, pattern)
Traceback (most recent call last):
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 817, in _parse
    raise Verbose
sre_parse.Verbose

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    nltk.regexp_tokenize(palabras_crudo, pattern)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 216, in regexp_tokenize
    return tokenizer.tokenize(text)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 123, in tokenize
    self._check_regexp()
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\site-packages\nltk\tokenize\regexp.py", line 120, in _check_regexp
    self._regexp = re.compile(self._pattern, self._flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\re.py", line 252, in compile
    return _compile(pattern, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\re.py", line 304, in _compile
    p = sre_compile.compile(pattern, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 956, in parse
    p = _parse_sub(source, state, True, 0)
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "C:\Users\chej_\AppData\Local\Programs\Python\Python39\lib\sre_parse.py", line 823, in _parse
    raise source.error("unknown extension ?" + char,
re.error: unknown extension ?; at position 157 (line 4, column 12)
>>> pattern = r'''(?x)          #set flag to allow verbose regexps
		(?:[A-Z]\.)+	#abbreviations, e.g. U.S.A.
		| \w+(?:\w+)*	#words with optional integral hyphens
		| \$?\d+(?:\.\d+)?%?	#currency and percentages, e.g. $12.40, 82%
		| \.\.\.	#elipsis
		| [][.,;"'?():-_`] #there are separate tokens; includes ], [ '''
>>> nltk.regexp_tokenize(palabras_crudo, pattern)[:50]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed', 'in', 'boxes', 'toast', 'each', 'other', '.', 'Doors', 'closing', '...', 'BAM', 'â', 'from', 'behind', 'the', 'orchestra', 'â', 'TERRORISTS', 'with', 'MACHINE', 'GUNS', 'BURST', 'in', '...', 'The', 'audience', 'SCREAMS', '...', 'The', 'terrorists', 'cover', 'the', 'ordinary', 'people', 'â', 'the']
>>> sents = nltk.sent_tokenize(palabras_crudo)
>>> pprint.pprint(sents[79:89])
['At \n'
 'the bullet hole the PUFF OF SMOKE THICKENS... \n'
 '5.\n'
 'the Protagonist, confused, REACHES towards it... the SWAT \n'
 'COCKS his weapon...\n'
 'BLAM!',
 'With EXPLOSIVE FORCE THE BULLET HOLE DISAPPEARS â\x80\x93 A \n'
 'NICK HAS APPEARED IN THE PROTAGONISTâ\x80\x99S UNIFORM â\x80\x93 he SPINS '
 'â\x80\x93 \n'
 'the SWAT is SHOT THROUGH THE CHEST AND DROPS... revealing a \n'
 'FIGURE, also in a gas mask and tactical gear...',
 'The Figure TURNS â\x80\x93 the Protagonist sees, on the Figureâ\x80\x99s \n'
 'pack, a small TALISMAN â\x80\x93 a COIN with a hole tied to a zip by \n'
 'ORANGE AND YELLOW THREAD â\x80\x93 the Protagonist turns back to grab \n'
 'the bomb â\x80\x93\n'
 'â\x80\x98TARGETâ\x80\x99\n'
 'That wasnâ\x80\x99t one of us.',
 'PROTAGONIST\nIâ\x80\x99ll take the help.',
 'The Protagonist GRABS the last bomb: â\x80\x980:03â\x80\x99... he looks up '
 'to \n'
 'the boxes, where REAL SWATS EVACUATE THE HIGH OFFICIALS...',
 'THE PROTAGONIST LOBS THE BOMBS UP INTO THE BOXES...\nEXT.',
 'PLAZA, DOWNTOWN KIEV â\x80\x93 CONTINUOUS\n'
 'The Protagonist and â\x80\x98Targetâ\x80\x99 emerge â\x80\x93 an EXPLOSION '
 'above them \n'
 '-\n'
 'INT.',
 'THEATRE, CONCERT HALL â\x80\x93 CONTINUOUS\n'
 'INNOCENT CIVILIANS STIR under the EXPLOSION IN THE BOXES â\x80\x93\n'
 'EXT.',
 'PLAZA, DOWNTOWN KIEV â\x80\x93 CONTINUOUS\n'
 'The van PULLS UP â\x80\x93 rear door open â\x80\x93 they JUMP INSIDE '
 'â\x80\x93\n'
 'INT.',
 'VAN â\x80\x93 MOMENTS LATER\nThe Protagonist pulls off his mask.']
>>> pprint.pprint(sents[:15])
['TENET\nWritten by\nChristopher Nolan\nORCHESTRA TUNING, audience settling.',
 'High officials in \nglassed-in boxes toast each other.',
 'Doors closing...\n'
 'BAM â\x80\x93 from behind the orchestra â\x80\x93 TERRORISTS with MACHINE \n'
 'GUNS BURST in...',
 'The audience SCREAMS...',
 'The terrorists cover \n'
 'the ordinary people â\x80\x93 the HIGH OFFICIALS are held in the \n'
 'BOXES...\n'
 'INT./EXT.',
 'VAN, PLAZA, DOWNTOWN KIEV, UKRAINE â\x80\x93 DAY\n'
 'As POLICE FLOOD THE PLAZA, the DRIVER turns to the PASSENGER \n'
 'â\x80\x93\n'
 'DRIVER\n'
 '(in Ukrainian)\n'
 'â\x80\x93 Wake up the Americans.',
 'â\x80\x93\n'
 'The Passenger turns to the back where four BLACK-CLAD YOUNG \n'
 'MEN SIT, WAITING.',
 'The nearest one seems to be SLEEPING...',
 'PASSENGER\n'
 'Hey â\x80\x93\n'
 'EYES CLOSED, the young man COCKS his weapon, chambering a \n'
 'round, POPS it out of the slide, CATCHES it, opens his eyes â\x80\x93 \n'
 'this is THE PROTAGONIST...',
 'The Passenger nods, â\x80\x98okayâ\x80\x99.',
 'The Driver looks down at a \nVARIETY OF UNIFORM PATCHES...\nSIRENS.',
 'The Americans shoulder WEAPONS, pull on HELMETS...\n'
 'A UKRAINIAN SWAT VAN SCREECHES to a halt outside the theatre \n'
 'â\x80\x93\n'
 'The Passenger spots its markings â\x80\x93 TOSSES the corresponding \n'
 'patches to the Americans, who slap them onto their shoulders.',
 'Ukrainian SWATs pour out of the SWAT van â\x80\x93\n'
 'The Americans JUMP out of the back of their van, SLIPPING \n'
 'UNNOTICED INTO THE STREAM OF SWATS pouring into the lobby...\n'
 'INT.',
 'LOBBY, CONCERT HALL â\x80\x93 CONTINUOUS\n'
 'SWATs mass at each entrance... the Protagonist watches GAS \n'
 'CANISTERS brought in TO THE AIR-CONDITIONING SYSTEM.',
 'The \nSWATs pull on GAS MASKS...\nINT.']
>>> text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
>>> seg1 = "0000000000000001000000000010000000000000000100000000000"
>>> seg2 = "0100100100100001001001000010100100010010000100010010000"
>>> def segment(text, segs):
	words = []
	last = 0
	for i in range(len(segs)):
		if segs[i] == '1':
			words.append(text[last:i+1])
			last = i+1
		words.append(text[last:])
		return words

	
>>> segment(text, seg1)
['doyouseethekittyseethedoggydoyoulikethekittylikethedoggy']
>>> segment(text, seg2)
['doyouseethekittyseethedoggydoyoulikethekittylikethedoggy']
>>> def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i+1
    words.append(text[last:])
    return words

>>> segment(text, seg2)
['do', 'you', 'see', 'the', 'kitty', 'see', 'the', 'doggy', 'do', 'you', 'like', 'the', 'kitty', 'like', 'the', 'doggy']
>>> segment(text, seg1)
['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
>>> def evaluate(text, segs):
    words = segment(text, segs)
    text_size = len(words)
    lexicon_size = sum(len(word) + 1 for word in set(words))
    return text_size + lexicon_size

>>> seg3 = "0000100100000011001000000110000100010000001100010000001"
>>> segment(text, seg3)
['doyou', 'see', 'thekitt', 'y', 'see', 'thedogg', 'y', 'doyou', 'like', 'thekitt', 'y', 'like', 'thedogg', 'y']
>>> evaluate(text, seg3)
47
>>> evaluate(text, seg2)
48
>>> evaluate(text, seg1)
64
>>> from random import randint
>>> def flip(segs, pos):
	return segs[:pos] + str(1-int(segs[pos])) + segs[pos+1:]

>>> def flip_n(segs, n):
	for i in range(n):
		segs = flip(segs, randint(0, len(segs)-1))
	return segs

>>> def anneal(text, segs, iterations, cooling_rate):
	temperature = float(len(segs))
	while temperature > 0.5:
		best_segs, best = segs, evaluate(text, segs)
		for i in range(iterations):
			guess = flip_n(segs, round(temperature))
			score = evaluate(text, guess)
			if score < best:
				best, best_segs = score, guess
		score, segs = best, best_segs
		temperature = temperature / cooling_rate
		print(evaluate(text, segs), segment(text, segs))
	print()
	return segs

>>> anneal(text, seg1, 5000, 1.2)
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
64 ['doyouseethekitty', 'seethedoggy', 'doyoulikethekitty', 'likethedoggy']
60 ['doyous', 'eeth', 'ekittysee', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
60 ['doyous', 'eeth', 'ekittysee', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
56 ['doyou', 'seeth', 'eki', 'ttysee', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
56 ['doyou', 'seeth', 'eki', 'ttysee', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
52 ['doyou', 'see', 'th', 'ekitty', 's', 'ee', 'thedoggy', 'doyou', 'like', 'th', 'ekitty', 'like', 'thedoggy']
50 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'li', 'ke', 'thedoggy']
49 ['doyou', 'see', 'thekitty', 's', 'ee', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']
43 ['doyou', 'see', 'thekitty', 'see', 'thedoggy', 'doyou', 'like', 'thekitty', 'like', 'thedoggy']

'0000100100000001001000000010000100010000000100010000000'

>>> silly = ['We', 'called', 'him', 'Tortoise', 'because', 'he', 'taught', 'us', '.']
>>> ' '.join(silly)
'We called him Tortoise because he taught us .'
>>> ';'.join(silly)
'We;called;him;Tortoise;because;he;taught;us;.'
>>> ''.join(silly)
'WecalledhimTortoisebecausehetaughtus.'
>>> fdist = nltk.FreqDist(['dog', 'cat', 'dog', 'cat', 'dog', 'snake', 'dog', 'cat'])
>>> for word in sorted(fdist):
	print(word, '-<->', fdist[word], end='; ')

	
cat -<-> 3; dog -<-> 4; snake -<-> 1; 
>>> for word in sorted(fdist):
	print('{}->{};'.format(word, fdist[word]), end=' ')

	
cat->3; dog->4; snake->1; 
>>> '{}->'.format('cat')
'cat->'
>>> '{} wants a {}'.format ('Lee', 'sandwich', 'for lunch')
'Lee wants a sandwich'
>>> template = 'Lee wants a {} right now'
>>> menu = ['sandwich', 'spam fritter', 'pancake']
>>> for snack in menu:
	print(template.format(snack))

	
Lee wants a sandwich right now
Lee wants a spam fritter right now
Lee wants a pancake right now
>>> '{:6}'.format(41)
'    41'
>>> '{<:6}'.format(41)
Traceback (most recent call last):
  File "<pyshell#225>", line 1, in <module>
    '{<:6}'.format(41)
KeyError: '<'
>>> '{:<6}'.format(41)
'41    '
>>> '{:<6}'.format('dog')
'dog   '
>>> '{:>6}'.format('dog')
'   dog'
>>> '{:6}'.format('dog')
'dog   '
>>> import math
>>> '{:.4f}'.format(math.pi)
'3.1416'
>>> '{:12.f}'.format(math.pi)
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    '{:12.f}'.format(math.pi)
ValueError: Format specifier missing precision
>>> '{:.12f}'.format(math.pi)
'3.141592653590'
>>> count, total = 3205, 9375
>>> 'accuracy for {} words: {:.4%}'.format(total, count / total)
'accuracy for 9375 words: 34.1867%'
>>> def tabulate(cfdist, words, categories):
	print('{16}'.format('Category'), end=' ')#column headings
	for word in words:
		print('{:<6}'.format(word), end=' ')
	print()
	for category in categories
	
SyntaxError: invalid syntax
>>> def tabulate(cfdist, words, categories):
	print('{16}'.format('Category'), end=' ')#column headings
	for word in words:
		print('{:>6}'.format(word), end=' ')
	print()
	for category in categories:
		print('{:16}'.format(category), end=' ')#row heading
		for word in words:#for each word
			pritn('{:6}'.format(cfdist[category][word]), end=' ')#print table
			print()

			
>>> def tabulate(cfdist, words, categories):
	print('{:16}'.format('Category'), end=' ')#column headings
	for word in words:
		print('{:>6}'.format(word), end=' ')
	print()
	for category in categories:
		print('{:16}'.format(category), end=' ')#row heading
		for word in words:#for each word
			pritn('{:6}'.format(cfdist[category][word]), end=' ')#print table
			print()

			
>>> def tabulate(cfdist, words, categories):
	print('{:16}'.format('Category'), end=' ')#column headings
	for word in words:
		print('{:>6}'.format(word), end=' ')
	print()
	for category in categories:
		print('{:16}'.format(category), end=' ')#row heading
		for word in words:#for each word
			print('{:6}'.format(cfdist[category][word]), end=' ')#print table
			print()

			
>>> from nltk.corpus import brown
>>> cfd = nltk.ConditionalFreqDist(
		(genre, word)
		for genre in brown.categories()
		for word in brown.words(categories=genre))


>>> genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
>>> modals = ['can', 'could', 'may', 'might', 'must', 'will']
>>> tabulate(cfd,modals,genres)
Category            can  could    may  might   must   will 
news                 93 
    86 
    66 
    38 
    50 
   389 
religion             82 
    59 
    78 
    12 
    54 
    71 
hobbies             268 
    58 
   131 
    22 
    83 
   264 
science_fiction      16 
    49 
     4 
    12 
     8 
    16 
romance              74 
   193 
    11 
    51 
    45 
    43 
humor                16 
    30 
     8 
     8 
     9 
    13 
>>> def tabulate(cfdist, words, categories):
    print('{:16}'.format('Category'), end=' ')                    # column headings
    for word in words:
        print('{:>6}'.format(word), end=' ')
    print()
    for category in categories:
        print('{:16}'.format(category), end=' ')                  # row heading
        for word in words:                                        # for each word
            print('{:6}'.format(cfdist[category][word]), end=' ') # print table cell
        print()

        
>>> tabulate(cfd,modals,genres)
Category            can  could    may  might   must   will 
news                 93     86     66     38     50    389 
religion             82     59     78     12     54     71 
hobbies             268     58    131     22     83    264 
science_fiction      16     49      4     12      8     16 
romance              74    193     11     51     45     43 
humor                16     30      8      8      9     13 
>>> output_file = open('output.txt', 'w')
>>> words = set(nltk.corpus.genesis.words('english-kjv.txt'))
>>> for word in sorted(words):
	print(word, file = output_file)

	
>>> len(words)
2789
>>> str(len(words))
'2789'
>>> print(str(len(words)), file = output_file)
>>> saying = ['After', 'all', 'is', 'said', 'and', 'done', ',',
...           'more', 'is', 'said', 'than', 'done', '.']
SyntaxError: invalid syntax
>>> saying = ['After', 'all', 'is', 'said', 'and', 'done', ',','more', 'is', 'said', 'than', 'done', '.']
>>> for word in saying:
	print(word, '(' + str(len(word)) + '),', end=' ')

	
After (5), all (3), is (2), said (4), and (3), done (4), , (1), more (4), is (2), said (4), than (4), done (4), . (1), 
>>> from textwrap import fill
>>> pieces = ['{}{}'.format(word,len(word)) for word in saying]
>>> output = ' '.join(pieces)
>>> wrapped = fill(output)
>>> print(wrapped)
After5 all3 is2 said4 and3 done4 ,1 more4 is2 said4 than4 done4 .1
>>> pieces = ['{} {}'.format(word, len(word)) for word in saying]
>>> output = ' '.join(pieces)
>>> wrapped = fill(output)
>>> print(wrapped)
After 5 all 3 is 2 said 4 and 3 done 4 , 1 more 4 is 2 said 4 than 4
done 4 . 1
>>> [w for w in tokens if re.findall('^wh',w)]
['where', 'who', 'who', 'who', 'where', 'which', 'while', 'who', 'what', 'what', 'what', 'which', 'which', 'whereâ\x80\x99d', 'what', 'where', 'what', 'what', 'whoâ\x80\x99s', 'who', 'whoâ\x80\x99s', 'who', 'whose', 'while', 'whatever', 'which', 'why', 'what', 'what', 'whoâ\x80\x99s', 'where', 'which', 'where', 'when', 'where', 'who', 'where', 'who', 'what', 'where', 'when', 'whoâ\x80\x99d', 'whoâ\x80\x99ve', 'when', 'whispers', 'what', 'what', 'whatever', 'where', 'wheels', 'where', 'where', 'whisper', 'which', 'whose', 'which', 'which', 'what', 'whyâ\x80\x99d', 'when', 'what', 'what', 'why', 'what', 'what', 'when', 'where', 'who', 'what', 'who', 'who', 'what', 'wheel', 'wheel', 'who', 'wheel', 'who', 'what', 'what', 'what', 'what', 'what', 'who', 'what', 'who', 'who', 'who', 'why', 'whatever', 'where', 'whatâ\x80\x99s', 'where', 'what', 'what', 'who', 'where', 'when', 'who', 'which', 'which', 'which', 'which', 'which', 'which', 'what', 'which', 'which', 'wheels', 'who', 'which', 'who', 'whirl', 'what', 'who', 'where', 'which', 'what', 'what', 'where', 'what', 'where', 'what', 'who', 'what', 'wheeling', 'where', 'what', 'whatever', 'where', 'what', 'what', 'what', 'whole', 'wheel', 'which', 'where', 'wheel', 'which', 'where', 'where', 'wheel', 'whatâ\x80\x99s', 'why', 'what', 'who', 'who', 'what', 'which', 'who', 'who', 'where', 'who', 'when', 'who', 'what', 'whose', 'what', 'where', 'when', 'what', 'why', 'who', 'why', 'what', 'where', 'when', 'whether', 'whoeverâ\x80\x99s', 'who', 'what', 'where', 'what', 'what', 'where', 'what', 'what', 'where', 'what', 'whole', 'while', 'who', 'who', 'who', 'who', 'whose', 'which', 'who', 'where', 'what', 'whole', 'who', 'what', 'whimper', 'where', 'where', 'what', 'what', 'which', 'whose', 'where', 'who', 'what', 'what', 'who', 'wheel', 'whoâ\x80\x99s', 'when', 'who', 'what', 'who', 'when', 'whole', 'what', 'what', 'what', 'whose']
>>> 
=========== RESTART: C:\Users\chej_\Documents\Filomemia\filomemia.py ===========
3510
>>> [w for w in tokens if re.findall('^wh',w)]
['where', 'who', 'who', 'who', 'where', 'which', 'while', 'who', 'what', 'what', 'what', 'which', 'which', 'whereâ\x80\x99d', 'what', 'where', 'what', 'what', 'whoâ\x80\x99s', 'who', 'whoâ\x80\x99s', 'who', 'whose', 'while', 'whatever', 'which', 'why', 'what', 'what', 'whoâ\x80\x99s', 'where', 'which', 'where', 'when', 'where', 'who', 'where', 'who', 'what', 'where', 'when', 'whoâ\x80\x99d', 'whoâ\x80\x99ve', 'when', 'whispers', 'what', 'what', 'whatever', 'where', 'wheels', 'where', 'where', 'whisper', 'which', 'whose', 'which', 'which', 'what', 'whyâ\x80\x99d', 'when', 'what', 'what', 'why', 'what', 'what', 'when', 'where', 'who', 'what', 'who', 'who', 'what', 'wheel', 'wheel', 'who', 'wheel', 'who', 'what', 'what', 'what', 'what', 'what', 'who', 'what', 'who', 'who', 'who', 'why', 'whatever', 'where', 'whatâ\x80\x99s', 'where', 'what', 'what', 'who', 'where', 'when', 'who', 'which', 'which', 'which', 'which', 'which', 'which', 'what', 'which', 'which', 'wheels', 'who', 'which', 'who', 'whirl', 'what', 'who', 'where', 'which', 'what', 'what', 'where', 'what', 'where', 'what', 'who', 'what', 'wheeling', 'where', 'what', 'whatever', 'where', 'what', 'what', 'what', 'whole', 'wheel', 'which', 'where', 'wheel', 'which', 'where', 'where', 'wheel', 'whatâ\x80\x99s', 'why', 'what', 'who', 'who', 'what', 'which', 'who', 'who', 'where', 'who', 'when', 'who', 'what', 'whose', 'what', 'where', 'when', 'what', 'why', 'who', 'why', 'what', 'where', 'when', 'whether', 'whoeverâ\x80\x99s', 'who', 'what', 'where', 'what', 'what', 'where', 'what', 'what', 'where', 'what', 'whole', 'while', 'who', 'who', 'who', 'who', 'whose', 'which', 'who', 'where', 'what', 'whole', 'who', 'what', 'whimper', 'where', 'where', 'what', 'what', 'which', 'whose', 'where', 'who', 'what', 'what', 'who', 'wheel', 'whoâ\x80\x99s', 'when', 'who', 'what', 'who', 'when', 'whole', 'what', 'what', 'what', 'whose']
>>> import unicodedata
>>> for c in palabras_crudo:
	if ord(c) > 127:
		print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

		
b'\xc3\xa2' U+00e2LATIN SMALL LETTER A WITH CIRCUMFLEX
Traceback (most recent call last):
  File "<pyshell#291>", line 3, in <module>
    print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))
ValueError: no such name
>>> for c in palabras_crudo:
	if ord(c) > 127:
		print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

		
b'\xc3\xa2' U+00e2LATIN SMALL LETTER A WITH CIRCUMFLEX
Traceback (most recent call last):
  File "<pyshell#293>", line 3, in <module>
    print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))
ValueError: no such name
>>> for c in vocabulario:
	if ord(c) > 127:
		print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

		
Traceback (most recent call last):
  File "<pyshell#295>", line 2, in <module>
    if ord(c) > 127:
TypeError: ord() expected a character, but string of length 5 found
>>> for c in tokens:
	if ord(c) > 127:
		print('{} U+{:04x}{}'.format(c.encode('utf8'), ord(c), unicodedata.name(c)))

		
Traceback (most recent call last):
  File "<pyshell#297>", line 2, in <module>
    if ord(c) > 127:
TypeError: ord() expected a character, but string of length 5 found
>>> for c in palabras_crudo:
	if ord(c) > 127:
		print('{} U+{:04x}{}'.format(c, ord(c), unicodedata.name(c)))

		
â U+00e2LATIN SMALL LETTER A WITH CIRCUMFLEX
Traceback (most recent call last):
  File "<pyshell#299>", line 3, in <module>
    print('{} U+{:04x}{}'.format(c, ord(c), unicodedata.name(c)))
ValueError: no such name
>>> palabras_crudo[:20]
'TENET\nWritten by\nChr'
>>> tokens[:20]
['TENET', 'Written', 'by', 'Christopher', 'Nolan', 'ORCHESTRA', 'TUNING', ',', 'audience', 'settling', '.', 'High', 'officials', 'in', 'glassed-in', 'boxes', 'toast', 'each', 'other', '.']
>>> tokens[20:80]
['Doors', 'closing', '...', 'BAM', 'â\x80\x93', 'from', 'behind', 'the', 'orchestra', 'â\x80\x93', 'TERRORISTS', 'with', 'MACHINE', 'GUNS', 'BURST', 'in', '...', 'The', 'audience', 'SCREAMS', '...', 'The', 'terrorists', 'cover', 'the', 'ordinary', 'people', 'â\x80\x93', 'the', 'HIGH', 'OFFICIALS', 'are', 'held', 'in', 'the', 'BOXES', '...', 'INT./EXT', '.', 'VAN', ',', 'PLAZA', ',', 'DOWNTOWN', 'KIEV', ',', 'UKRAINE', 'â\x80\x93', 'DAY', 'As', 'POLICE', 'FLOOD', 'THE', 'PLAZA', ',', 'the', 'DRIVER', 'turns', 'to', 'the']
>>> palabras_crudo[20:80]
'istopher Nolan\nORCHESTRA TUNING, audience settling. High off'
>>> palabras_crudo[300:400]
'H OFFICIALS are held in the \nBOXES...\nINT./EXT. VAN, PLAZA, DOWNTOWN KIEV, UKRAINE â\x80\x93 DAY\nAs POLICE'
>>> nacute.decode('â\x80\x93')
Traceback (most recent call last):
  File "<pyshell#305>", line 1, in <module>
    nacute.decode('â\x80\x93')
NameError: name 'nacute' is not defined
>>> nacute.encode('â\x80\x93')
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    nacute.encode('â\x80\x93')
NameError: name 'nacute' is not defined
>>> 'â\x80\x93'.decode('latin2')
Traceback (most recent call last):
  File "<pyshell#307>", line 1, in <module>
    'â\x80\x93'.decode('latin2')
AttributeError: 'str' object has no attribute 'decode'
>>> ('â\x80\x93').decode('latin2')
Traceback (most recent call last):
  File "<pyshell#308>", line 1, in <module>
    ('â\x80\x93').decode('latin2')
AttributeError: 'str' object has no attribute 'decode'
>>> ('â\x80\x93').encode('latin2')
b'\xe2\x80\x93'
>>> ('â\x80\x93').encode('utf8')
b'\xc3\xa2\xc2\x80\xc2\x93'
>>> vocabulario[20:80]
['action', 'activates', 'activity', 'actually', 'adds', 'adjusts', 'admire', 'admires', 'advance', 'afar', 'affair', 'affect', 'affixes', 'afraid', 'after', 'afterlife', 'afternoon', 'afterthought', 'afterwards', 'again', 'against', 'age', 'agent', 'ago', 'agreed', 'ahead', 'aim', 'aiming', 'aims', 'air', 'airframe', 'airlock', 'airport', 'alarm', 'alarms', 'algorithm', 'alien', 'alive', 'all', 'alley', 'allies', 'alloys', 'almost', 'alone', 'along', 'alongside', 'already', 'alright', 'also', 'always', 'am', 'amalfi', 'amassed', 'ambition', 'ambulance', 'ambush', 'ambushing', 'american', 'americans', 'ammunition']
>>> [w for w in vocabulario if re.findall('^wh',w)]
['wham', 'what', 'whatever', 'wheel', 'wheeler', 'wheeling', 'wheels', 'when', 'where', 'whether', 'which', 'whiff', 'while', 'whimper', 'whine', 'whirl', 'whisper', 'whispers', 'white', 'whitman', 'who', 'whoa', 'whole', 'whose', 'whummmmm', 'why']
>>> [w for w in vocabulario if re.findall('^wh(y|o|at|ich|en|ere)',w)]
['what', 'whatever', 'when', 'where', 'which', 'who', 'whoa', 'whole', 'whose', 'why']
>>> [w for w in vocabulario if re.findall('^wh(y|o|at|ich|en|ere|se)$',w)]
['what', 'when', 'where', 'which', 'who', 'why']
>>> [w for w in palabras_crudo if re.findall('^wh(y|o|at|ich|en|ere|se)$',w)]
[]
>>> [w for w in tokens if re.findall('^wh(y|o|at|ich|en|ere|se)$',w)]
['where', 'who', 'who', 'who', 'where', 'which', 'who', 'what', 'what', 'what', 'which', 'which', 'what', 'where', 'what', 'what', 'who', 'who', 'which', 'why', 'what', 'what', 'where', 'which', 'where', 'when', 'where', 'who', 'where', 'who', 'what', 'where', 'when', 'when', 'what', 'what', 'where', 'where', 'where', 'which', 'which', 'which', 'what', 'when', 'what', 'what', 'why', 'what', 'what', 'when', 'where', 'who', 'what', 'who', 'who', 'what', 'who', 'who', 'what', 'what', 'what', 'what', 'what', 'who', 'what', 'who', 'who', 'who', 'why', 'where', 'where', 'what', 'what', 'who', 'where', 'when', 'who', 'which', 'which', 'which', 'which', 'which', 'which', 'what', 'which', 'which', 'who', 'which', 'who', 'what', 'who', 'where', 'which', 'what', 'what', 'where', 'what', 'where', 'what', 'who', 'what', 'where', 'what', 'where', 'what', 'what', 'what', 'which', 'where', 'which', 'where', 'where', 'why', 'what', 'who', 'who', 'what', 'which', 'who', 'who', 'where', 'who', 'when', 'who', 'what', 'what', 'where', 'when', 'what', 'why', 'who', 'why', 'what', 'where', 'when', 'who', 'what', 'where', 'what', 'what', 'where', 'what', 'what', 'where', 'what', 'who', 'who', 'who', 'who', 'which', 'who', 'where', 'what', 'who', 'what', 'where', 'where', 'what', 'what', 'which', 'where', 'who', 'what', 'what', 'who', 'when', 'who', 'what', 'who', 'when', 'what', 'what', 'what']
>>> 